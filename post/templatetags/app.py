from django import template

from post.models import Category

register = template.Library()


@register.inclusion_tag("tags/category.html")
def categories():
    return {
        'categories': Category.objects.all()
    }
