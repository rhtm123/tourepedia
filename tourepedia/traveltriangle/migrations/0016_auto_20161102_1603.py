# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-02 10:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0015_auto_20161102_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetail',
            name='start_day',
            field=models.DateField(blank=True, default=datetime.datetime.now),
        ),
    ]
