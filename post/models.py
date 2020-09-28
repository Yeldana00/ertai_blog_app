import uuid

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


class Category(models.Model):
    """ Барлық санаттар """

    name = models.CharField(max_length=30)
    slug = models.SlugField(max_length=100, unique=True)
    position = models.IntegerField(default=0, unique=True)
    post_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"
        verbose_name_plural = "Санаттар"
        ordering = ['-position']


def post_image_path(instance, filename):
    ext = filename.split('.')[-1]
    return 'images/post/{}.{}'.format(uuid.uuid4(), ext)


class Post(models.Model):
    """ Барлық посттарды сақтауға арналған """

    title = models.CharField("Тақырыбы", max_length=255)
    slug = models.SlugField("Слоган", unique=True)
    excerpt_text = models.TextField("Қысқа текст")
    text = models.TextField("Мәтіні")
    views_count = models.IntegerField("Қаралым саны", default=0, editable=False)
    comments_count = models.IntegerField("Пікірлер саны", default=0, editable=False)
    thumbnail_image = models.ImageField("Суреті", null=True, blank=True, upload_to=post_image_path)
    owner = models.ForeignKey(verbose_name="Автор", to=User, default=1, on_delete=models.CASCADE)
    category = models.ManyToManyField(verbose_name="Санат", to=Category)
    meta_key = models.TextField("Мета кілттер", blank=True, null=True)
    meta_description = models.TextField("Мета ақпарат", blank=True, null=True)
    is_published = models.BooleanField("Жарияланды ма?", default=False)
    created_at = models.DateTimeField("Қосылған күні", null=True, editable=False)
    updated_at = models.DateTimeField("Өзгертілген күні", null=True, editable=False)

    def get_absolute_url(self):
        return "/{}-{}.html".format(self.pk, self.slug)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_at = timezone.now()
        self.updated_at = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "posts"
        verbose_name_plural = "Жазбалар"
        ordering = ['-created_at']
