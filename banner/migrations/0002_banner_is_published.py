# Generated by Django 3.0.3 on 2020-08-20 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='banner',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
    ]
