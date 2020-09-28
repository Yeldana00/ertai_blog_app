from django.db import models


class Page(models.Model):
    name = models.CharField(verbose_name="Аты", max_length=30, default=None)
    slug = models.CharField(verbose_name="Слоган", max_length=255, default=None)
    text = models.TextField(verbose_name="Текст", )
    views_count = models.IntegerField(verbose_name="Қаралым саны", default=0, editable=False)
    is_published = models.BooleanField(verbose_name="Жарияланды ма?", default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "pages"
