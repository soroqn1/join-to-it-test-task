from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions

from .models import Event
from .permissions import IsOrganizerOrReadOnly
from .serializers import EventSerializer


@extend_schema(
    summary="List all events or create a new event",
    tags=["Events"],
)
class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.select_related("organizer").all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticated]

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
