from django import template

from menu.services import get_nav_menu

register = template.Library()


@register.inclusion_tag('tags/nav_menu.html')
def nav_links():
    return {
        'links': get_nav_menu()
    }
