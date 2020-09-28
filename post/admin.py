from django.contrib import admin
from django.contrib.admin import SimpleListFilter
from django_summernote.admin import SummernoteModelAdmin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from post.models import Post, Category


class PostResource(resources.ModelResource):
    class Meta:
        model = Post


class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category


class NullCategoryFilter(SimpleListFilter):
    title = 'Null status'  # a label for our filter
    parameter_name = 'none'  # you can put anything here

    def lookups(self, request, model_admin):
        return [
            ('category', 'Category')
        ]

    def queryset(self, request, queryset):
        return queryset.filter(category__isnull=True)


class PostAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    list_display = ('title', 'views_count', 'comments_count', 'is_published', 'created_at')
    search_fields = ('text',)
    list_editable = ('is_published',)
    summernote_fields = ('text', 'excerpt_text')
    rosource_class = PostResource
    list_per_page = 30


class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ('name', 'slug')


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
