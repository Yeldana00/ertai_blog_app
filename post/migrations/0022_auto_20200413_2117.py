# Generated by Django 3.0.3 on 2020-04-13 15:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20200407_2227'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='description',
            new_name='excerpt_text',
        ),
    ]
