# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-08 07:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0023_auto_20161108_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripdetail',
            name='source',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
