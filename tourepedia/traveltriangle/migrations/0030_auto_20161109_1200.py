# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-09 06:30
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0029_auto_20161109_1155'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripdetail',
            name='pub_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now, null=True),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='source',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
    ]
