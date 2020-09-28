import os
import uuid

from django.db import models

BANNER_TYPE_IMAGE = 'image'
BANNER_TYPE_CODE = 'code'

BANNER_TYPE = (
    ('image', 'Сурет'),
    ('code', 'Код')
)

BANNER_SPACE = (
    ('sidebar', 'Sidebar'),
    ('post_bottom', 'Post bottom')
)


def banner_upload_path(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join('images/banners', filename)


class Banner(models.Model):
    name = models.CharField(max_length=20, default=None)
    type = models.CharField(choices=BANNER_TYPE, max_length=10)
    image = models.ImageField(null=True, blank=True, upload_to=banner_upload_path)
    code = models.TextField(null=True, blank=True)
    space = models.CharField(choices=BANNER_SPACE, default='sidebar', max_length=30)
    url = models.URLField(null=True, blank=True)
    position = models.IntegerField(default=None)
    is_published = models.BooleanField(default=False)

    class Meta:
        db_table = "banners"
