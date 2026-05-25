from rest_framework import serializers

from apps.posts.models import Post


class PostSerializer(serializers.ModelSerializer):

    user = serializers.SerializerMethodField()

    class Meta:
        model = Post

        fields = [
            'id',
            'title',
            'content',
            'is_published',
            'user',
            'created_at'
        ]

    def get_user(self, obj):

        return {
            'id': obj.user.id,
            'username': obj.user.username,
            'email': obj.user.email,
        }


class CreatePostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post

        fields = [
            'title',
            'content',
            'is_published'
        ]