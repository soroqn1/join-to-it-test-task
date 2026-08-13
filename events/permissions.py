from rest_framework import permissions


class IsOrganizerOrReadOnly(permissions.BasePermission):
    """Custom permission to only allow organizers of an event to edit or delete it."""

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any safe request (GET, HEAD, OPTIONS)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the organizer of the event
        return obj.organizer == request.user
