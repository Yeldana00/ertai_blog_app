from django.db.models import F

from page.models import Page


def get_pages():
    """ Барлық жарияланған парақшаларды алу """
    return Page.objects.filter(is_published=True)


def get_page(page_id):
    """ ID бойынша парақты қайтару """
    return get_pages().get(id=page_id)


def update_page_views_count(page_id):
    """ ID бойынша қаралым санын жаңалау """
    Page.objects.filter(id=page_id).update(views_count=F('views_count') + 1)
