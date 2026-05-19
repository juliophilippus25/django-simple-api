from django.urls import path

from apps.authentication.views.auth_view import RegisterView


urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),
]