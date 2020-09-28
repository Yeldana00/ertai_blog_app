from django import template

from banner.services import get_sidebar_banners, get_post_bottom_banners

register = template.Library()


@register.inclusion_tag('tags/sidebar_banners.html')
def sidebar_banners():
    return {
        'banners': get_sidebar_banners()
    }


@register.inclusion_tag('tags/post_bottom_banners.html')
def post_bottom_banners():
    return {
        'banners': get_post_bottom_banners()
    }
