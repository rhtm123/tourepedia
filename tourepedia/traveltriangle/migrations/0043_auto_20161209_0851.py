# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-09 03:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0042_auto_20161209_0837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetail',
            name='start_day',
            field=models.DateField(auto_now_add=True),
        ),
    ]
