from banner.models import Banner


def get_banners():
    return Banner.objects.filter(is_published=True)


def get_sidebar_banners():
    return get_banners().filter(space="sidebar").order_by('position')


def get_post_bottom_banners():
    return get_banners().filter(space="post_bottom").order_by('position')
