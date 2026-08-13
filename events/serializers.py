from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Event, Registration


class RegistrationSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    event_id = serializers.IntegerField(source="event.id", read_only=True)

    class Meta:
        model = Registration
        fields = ("id", "user", "event_id", "registered_at")
        read_only_fields = ("id", "user", "event_id", "registered_at")


class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)
    registrations_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "date",
            "location",
            "organizer",
            "registrations_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "id",
            "organizer",
            "registrations_count",
            "created_at",
            "updated_at",
        )

    def get_registrations_count(self, obj) -> int:
        return obj.registrations.count()
