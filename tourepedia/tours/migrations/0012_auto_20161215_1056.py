# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-15 05:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0022_hotel_starting_price'),
        ('tours', '0011_auto_20161215_0950'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='importantpoint',
            name='imp_point',
        ),
        migrations.RemoveField(
            model_name='touritinerary',
            name='tour_stay',
        ),
        migrations.AddField(
            model_name='importantpoint',
            name='imp_points',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='touritinerary',
            name='tour_stays',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel'),
        ),
    ]
