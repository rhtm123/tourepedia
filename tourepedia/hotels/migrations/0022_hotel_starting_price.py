# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-11 11:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0021_hotel_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='starting_price',
            field=models.IntegerField(null=True),
        ),
    ]
