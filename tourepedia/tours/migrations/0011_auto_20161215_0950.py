# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-15 04:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0010_auto_20161215_0934'),
    ]

    operations = [
        migrations.AddField(
            model_name='importantpoint',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='importantpoint',
            name='imp_point',
            field=models.TextField(blank=True, null=True),
        ),
    ]
