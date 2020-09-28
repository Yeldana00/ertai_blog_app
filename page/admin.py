from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from page.models import Page


class PageAdmin(SummernoteModelAdmin):
    list_display = ('name', 'views_count', 'is_published')
    list_editable = ('is_published',)
    summernote_fields = ('text',)


admin.site.register(Page, PageAdmin)
