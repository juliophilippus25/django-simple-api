from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework_simplejwt.views import TokenRefreshView

from apps.authentication.serializers.auth_serializer import RegisterSerializer, LoginSerializer
from apps.authentication.services.auth_service import register_user, login_user

from apps.core.responses import (
    success_response,
    error_response
)

# Register
class RegisterView(APIView):

    permission_classes = []

    def post(self, request):

        serializer = RegisterSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        user = register_user(
            serializer.validated_data
        )

        return success_response(
            message='Register success',
            data={
                'id': user.id,
                'username': user.username,
                'email': user.email,
            },
            status_code=201
        )

# Login
class LoginView(APIView):

    permission_classes = []

    def post(self, request):

        serializer = LoginSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        result = login_user(
            email=serializer.validated_data['email'],
            password=serializer.validated_data['password']
        )

        return success_response(
            message='Login success',
            data=result
        )

# Me
class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        user = request.user

        return success_response(
            message='User fetched successfully',
            data={
                'id': user.id,
                'username': user.username,
                'email': user.email,
                'full_name': user.full_name,
                'phone': user.phone,
            }
        )

# Refresh
class CustomRefreshView(TokenRefreshView):

    permission_classes = []

    def post(self, request, *args, **kwargs):

        response = super().post(
            request,
            *args,
            **kwargs
        )

        return success_response(
            message='Token refreshed successfully',
            data={
                'access_token': response.data['access']
            }
        )