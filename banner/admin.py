from django.contrib import admin

from banner.models import Banner


class BannerAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'space', 'is_published')
    list_editable = ('is_published', 'type', 'space')


admin.site.register(Banner, BannerAdmin)