from django.contrib.auth import get_user_model
from drf_spectacular.utils import extend_schema
from rest_framework import generics, permissions
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from .serializers import RegisterSerializer, UserSerializer

User = get_user_model()


@extend_schema(summary="Register a new user", tags=["Auth"])
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer


@extend_schema(summary="Obtain JWT token pair (login)", tags=["Auth"])
class CustomTokenObtainPairView(TokenObtainPairView):
    permission_classes = [permissions.AllowAny]


@extend_schema(summary="Refresh JWT access token", tags=["Auth"])
class CustomTokenRefreshView(TokenRefreshView):
    permission_classes = [permissions.AllowAny]


@extend_schema(summary="Retrieve or update current user profile", tags=["Users"])
class UserProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user
