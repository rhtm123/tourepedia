# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-28 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_auto_20160916_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='title',
            name='blog_type',
            field=models.CharField(choices=[('inspired', 'Be Inspired'), ('photoblog', 'Photo Blog'), ('tips', 'Travel Tips'), ('stories', 'Travel Stories')], max_length=128, null=True),
        ),
    ]
