# Generated by Django 4.1 on 2022-09-02 00:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainblog', '0007_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost', to=settings.AUTH_USER_MODEL),
        ),
    ]
