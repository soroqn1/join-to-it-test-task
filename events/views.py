from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import filters, generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .filters import EventFilter
from .models import Event, Registration
from .permissions import IsOrganizerOrReadOnly
from .serializers import EventSerializer, RegistrationSerializer
from .tasks import send_registration_email


@extend_schema(
    summary="List all events or create a new event",
    tags=["Events"],
)
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.select_related("organizer").all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = EventFilter
    search_fields = ["title", "description"]
    ordering_fields = ["date", "created_at"]
    ordering = ["-date"]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)


@extend_schema(
    summary="Retrieve, update or delete an event",
    tags=["Events"],
)
class EventDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.select_related("organizer").all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated, IsOrganizerOrReadOnly]


@extend_schema(
    summary="Register for an event or cancel registration",
    tags=["Registrations"],
)
class EventRegisterView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    @extend_schema(
        summary="Join an event",
        responses={201: RegistrationSerializer, 400: dict},
    )
    def post(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        registration, created = Registration.objects.get_or_create(user=request.user, event=event)

        if not created:
            return Response(
                {"detail": "You are already registered for this event."},
                status=status.HTTP_400_BAD_REQUEST,
            )

        send_registration_email.delay(
            user_email=request.user.email,
            event_title=event.title,
            event_date=str(event.date),
            location=event.location,
        )

        serializer = RegistrationSerializer(registration)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @extend_schema(
        summary="Cancel registration for an event",
        responses={204: None, 404: dict},
    )
    def delete(self, request, pk):
        event = get_object_or_404(Event, pk=pk)
        registration = Registration.objects.filter(user=request.user, event=event).first()

        if not registration:
            return Response(
                {"detail": "You are not registered for this event."},
                status=status.HTTP_404_NOT_FOUND,
            )

        registration.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
