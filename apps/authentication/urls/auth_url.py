from django.urls import path

from apps.authentication.views.auth_view import (
    RegisterView,
    LoginView,
    MeView,
    CustomRefreshView
)

urlpatterns = [
    path(
        'register/',
        RegisterView.as_view(),
        name='register'
    ),

    path(
        'login/',
        LoginView.as_view(),
        name='login'
    ),

    path(
        'me/',
        MeView.as_view(),
        name='me'
    ),

    path(
        'refresh/',
        CustomRefreshView.as_view(),
        name='token_refresh'
    ),
]