# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-10 08:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_auto_20160902_1216'),
    ]

    operations = [
        migrations.AddField(
            model_name='title',
            name='blog_type',
            field=models.CharField(choices=[('inspired', 'Be Inspired'), ('photoblog', 'Photo Blog'), ('tips', 'Travel Tips'), ('stories', 'Travel Stories')], max_length=128, null=True),
        ),
        migrations.AddField(
            model_name='title',
            name='state_detail',
            field=models.TextField(max_length=100000, null=True),
        ),
    ]