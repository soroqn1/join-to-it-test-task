from rest_framework import serializers

from users.serializers import UserSerializer

from .models import Event


class EventSerializer(serializers.ModelSerializer):
    organizer = UserSerializer(read_only=True)

    class Meta:
        model = Event
        fields = (
            "id",
            "title",
            "description",
            "date",
            "location",
            "organizer",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("id", "organizer", "created_at", "updated_at")
