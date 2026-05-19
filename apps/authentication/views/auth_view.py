from rest_framework.views import APIView
from rest_framework import status

from apps.authentication.serializers.auth_serializer import RegisterSerializer
from apps.authentication.services.auth_service import register_user

from apps.core.responses import (
    success_response,
    error_response
)


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