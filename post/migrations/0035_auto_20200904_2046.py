# Generated by Django 3.0.3 on 2020-09-04 14:46

from django.db import migrations, models
import post.models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0034_delete_wppostmeta'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to=post.models.post_image_path, verbose_name='Суреті'),
        ),
    ]