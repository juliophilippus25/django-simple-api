from rest_framework import serializers

from apps.authentication.models import User

# Register
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

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                'Email already exists'
            )

        return value

    def validate_username(self, value):

        if User.objects.filter(username=value).exists():
            raise serializers.ValidationError(
                'Username already exists'
            )

        return value

# Login
class LoginSerializer(serializers.Serializer):

    email = serializers.EmailField()

    password = serializers.CharField(
        write_only=True
    )