# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-17 06:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0016_auto_20160927_0826'),
        ('traveltriangle', '0036_auto_20161117_1208'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='itinerary',
            name='night_stay',
        ),
        migrations.AddField(
            model_name='itinerarydaywise',
            name='night_stay',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel'),
        ),
    ]
