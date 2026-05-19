from rest_framework import serializers

from apps.authentication.models import User


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = User

        fields = [
            'username',
            'email',
            'password',
            'full_name',
            'phone'
        ]

        extra_kwargs = {
            'password': {
                'write_only': True
            }
        }