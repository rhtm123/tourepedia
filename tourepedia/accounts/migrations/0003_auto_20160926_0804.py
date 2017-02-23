# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-26 02:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_userprofile_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userdetail',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userdetail',
            name='userprofile',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='picture',
            field=models.ImageField(blank=True, upload_to='img'),
        ),
        migrations.DeleteModel(
            name='UserDetail',
        ),
    ]