from django.urls import path

from apps.posts.views.post_view import (
    PostListCreateView,
    PostDetailView,
    MyPostView
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

    path(
        'my-posts/',
        MyPostView.as_view(),
        name='my_posts'
    ),
]