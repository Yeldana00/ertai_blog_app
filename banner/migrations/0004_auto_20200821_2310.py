# Generated by Django 3.0.3 on 2020-08-21 17:10

import banner.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0003_auto_20200821_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=banner.models.banner_upload_path),
        ),
    ]
