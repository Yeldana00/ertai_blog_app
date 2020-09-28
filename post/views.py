import requests
from django.http import JsonResponse
from django.shortcuts import redirect
from django.template.response import TemplateResponse
from django.urls import reverse
from django.views.generic import ListView
from requests.auth import HTTPBasicAuth

from post.services import get_posts, get_post, update_post_views_count, get_category_posts, get_post_by_slug, \
    get_category, get_recommendation_posts


class PostListView(ListView):
    queryset = get_posts()
    paginate_by = 30
    template_name = 'post/list.html'
    context_object_name = 'posts'


class PostListByCategoryView(ListView):
    paginate_by = 30
    template_name = 'post/list.html'
    context_object_name = 'posts'

    def get_context_data(self, **kwargs):
        context = super(PostListByCategoryView, self).get_context_data(**kwargs)
        context["category"] = get_category(self.kwargs.get("category"))
        return context

    def get_queryset(self):
        return get_category_posts(self.kwargs.get("category"))


def post_detail(request, post_id, slug):
    """ Постты толық ашып көрсетеді. Қаралым санын жаңалайды. Пост базада болмаса 404 қайтарады. """

    post = get_post(post_id)
    update_post_views_count(post_id)

    recommendation_posts = get_recommendation_posts(post_id, post.category)

    return TemplateResponse(request, 'post/detail.html', {
        "post": post,
        'recommended_posts': recommendation_posts
    })


def old_post_detail(request, slug):
    """ Ескі url мекенжайдан жаңасына редирект жасайды. """

    post = get_post_by_slug(slug)

    return redirect(reverse("post_detail", kwargs={
        "post_id": post.id,
        "slug": post.slug
    }))


def migrate_data(request):

    response = requests.post('https://ertai.kz/wp-json/wp/v2/posts', data={
        "title": "App"
    }, auth=HTTPBasicAuth(username="ertai", password="!3vLGEHg8$tCE2e4)E")).json()

    return JsonResponse(response)
