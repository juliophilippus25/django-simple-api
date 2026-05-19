from apps.authentication.models import User


def register_user(data):

    user = User.objects.create_user(
        username=data['username'],
        email=data['email'],
        password=data['password'],
        full_name=data.get('full_name'),
        phone=data.get('phone')
    )

    return user