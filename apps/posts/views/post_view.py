from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import NotFound

from apps.posts.serializers.post_serializer import (
    PostSerializer,
    CreatePostSerializer
)

from apps.posts.selectors.post_selector import (
    get_all_posts,
    get_post_by_id
)

from apps.posts.services.post_service import (
    create_post,
    update_post,
    delete_post
)

from apps.core.responses import success_response


class PostListCreateView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        posts = get_all_posts()

        serializer = PostSerializer(
            posts,
            many=True
        )

        return success_response(
            message='Posts fetched successfully',
            data=serializer.data
        )

    def post(self, request):

        serializer = CreatePostSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        post = create_post(
            request.user,
            serializer.validated_data
        )

        return success_response(
            message='Post created successfully',
            data=PostSerializer(post).data,
            status_code=201
        )


class PostDetailView(APIView):

    permission_classes = [IsAuthenticated]

    def get_object(self, post_id):

        post = get_post_by_id(post_id)

        if not post:
            raise NotFound(
                'Post not found'
            )

        return post

    def get(self, request, post_id):

        post = self.get_object(post_id)

        return success_response(
            message='Post fetched successfully',
            data=PostSerializer(post).data
        )

    def put(self, request, post_id):

        post = self.get_object(post_id)

        if post.user != request.user:
            raise NotFound(
                'Post not found'
            )

        serializer = CreatePostSerializer(
            data=request.data
        )

        serializer.is_valid(
            raise_exception=True
        )

        updated_post = update_post(
            post,
            serializer.validated_data
        )

        return success_response(
            message='Post updated successfully',
            data=PostSerializer(updated_post).data
        )

    def delete(self, request, post_id):

        post = self.get_object(post_id)

        if post.user != request.user:
            raise NotFound(
                'Post not found'
            )

        delete_post(post)

        return success_response(
            message='Post deleted successfully'
        )