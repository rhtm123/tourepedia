# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-05 05:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0021_auto_20161105_1110'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetail',
            name='budget',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
