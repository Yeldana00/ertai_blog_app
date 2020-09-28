from django.urls import path

from post.views import PostListView, post_detail, PostListByCategoryView, old_post_detail

urlpatterns = [
    path('', PostListView.as_view(), name="post_list"),
    path('category/<int:category>-<str:slug>.html', PostListByCategoryView.as_view(), name="category_posts"),
    path('<int:post_id>-<str:slug>.html', post_detail, name="post_detail"),
    path('blog/<str:slug>.html', old_post_detail)
]
