from apps.posts.models import Post


def create_post(user, data):

    post = Post.objects.create(
        user=user,
        title=data['title'],
        content=data['content'],
        is_published=data.get(
            'is_published',
            True
        )
    )

    return post


def update_post(post, data):

    post.title = data.get(
        'title',
        post.title
    )

    post.content = data.get(
        'content',
        post.content
    )

    post.is_published = data.get(
        'is_published',
        post.is_published
    )

    post.save()

    return post


def delete_post(post):

    post.delete()