# Generated by Django 3.0.1 on 2019-12-21 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0005_post_updated_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='comment_count',
            new_name='comments_count',
        ),
    ]
