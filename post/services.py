from django.db.models import F, Q

from post.models import Post, Category


def get_posts():
    return Post.objects.filter(is_published=True)


def get_post(post_id: int) -> Post:
    return get_posts().get(id=post_id)


def get_post_by_slug(slug: str) -> Post:
    return get_posts().get(slug=slug)


def get_category(category_id):
    return Category.objects.get(id=category_id)


def get_category_posts(category_id):
    get_category(category_id)
    return get_posts().filter(category__in=[category_id])


def get_recommendation_posts(post_id, categories):
    if categories:
        return Post.objects.filter(Q(category__in=[1]) & ~Q(id=post_id)).order_by('views_count')[:6]


def update_post_views_count(post_id):
    Post.objects.filter(id=post_id).update(views_count=F('views_count') + 1)
