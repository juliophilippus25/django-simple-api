from django.contrib.auth import authenticate

from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

from apps.authentication.models import User
from apps.authentication.selectors.auth_selector import (
    get_user_by_email
)


def register_user(data):

    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        full_name=data.get('full_name'),
        phone=data.get('phone')
    )

    return user


def login_user(email, password):

    user = get_user_by_email(email)

    if not user:
        raise AuthenticationFailed(
            'Invalid credentials'
        )

    auth_user = authenticate(
        username=user.username,
        password=password
    )

    if not auth_user:
        raise AuthenticationFailed(
            'Invalid credentials'
        )

    refresh = RefreshToken.for_user(user)

    return {
        'access_token': str(refresh.access_token),
        'refresh_token': str(refresh),
        'user': {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'full_name': user.full_name,
        }
    }