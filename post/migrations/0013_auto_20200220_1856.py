# Generated by Django 3.0.3 on 2020-02-20 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0012_auto_20200220_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='meta_key',
            field=models.TextField(default=None, null=True),
        ),
    ]
