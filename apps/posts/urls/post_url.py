from django.urls import path

from apps.posts.views.post_view import (
    PostListCreateView,
    PostDetailView
)


urlpatterns = [
    path(
        '',
        PostListCreateView.as_view(),
        name='post_list_create'
    ),

    path(
        '<uuid:post_id>/',
        PostDetailView.as_view(),
        name='post_detail'
    ),
]