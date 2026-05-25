from apps.posts.models import Post


def get_all_posts():

    return Post.objects.select_related(
        'user'
    ).all()


def get_post_by_id(post_id):

    return Post.objects.select_related(
        'user'
    ).filter(
        id=post_id
    ).first()