# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-02 08:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0014_auto_20161102_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetail',
            name='start_day',
            field=models.DateField(auto_now=True),
        ),
    ]
