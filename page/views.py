from django.shortcuts import render

from page.services import get_page, update_page_views_count


def page_detail(request, page_id, slug):

    page = get_page(page_id)
    update_page_views_count(page_id)

    return render(request, 'page/detail.html', {
        'page': page
    })
