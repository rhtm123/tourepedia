# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-04 03:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tripdetail',
            name='end_day',
        ),
        migrations.AddField(
            model_name='comment',
            name='quoted_price',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='tripdetail',
            name='trip_nights',
            field=models.IntegerField(null=True),
        ),
    ]
