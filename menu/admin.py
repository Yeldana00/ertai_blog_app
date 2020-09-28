from django.contrib import admin
from django.contrib.admin import ModelAdmin

from menu.models import Menu


class MenuAdmin(ModelAdmin):
    list_display = ('name', 'position', 'color')
    list_editable = ('position',)


admin.site.register(Menu, MenuAdmin)
