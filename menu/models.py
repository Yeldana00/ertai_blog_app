from django.db import models

from page.models import Page
from post.models import Category

MENU_TYPE_CATEGORY = "category"
MENU_TYPE_URL = "url"
MENU_TYPE_PAGE = "page"

MENU_TYPE = (
    ("url", "Сілтеме"),
    ("page", "Парақша")
)


class Menu(models.Model):
    name = models.CharField(max_length=30, default=None)
    category = models.ForeignKey(to=Category, on_delete=models.CASCADE, null=True, blank=True)
    page = models.ForeignKey(to=Page, on_delete=models.CASCADE, null=True, blank=True)
    url = models.URLField(null=True, blank=True)
    type = models.CharField(choices=MENU_TYPE, max_length=15, default=None)
    color = models.CharField(max_length=10, null=True, blank=True)
    position = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "menu_links"
