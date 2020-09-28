from django.urls import path

from page.views import page_detail

urlpatterns = [
    path('<int:page_id>-<str:slug>.html', page_detail, name="page_detail")
]
