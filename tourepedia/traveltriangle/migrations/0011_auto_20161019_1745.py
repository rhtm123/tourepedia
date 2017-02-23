# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-19 12:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0010_quotegeneration_night_stay'),
    ]

    operations = [
        migrations.AddField(
            model_name='quote',
            name='trip_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='quotegeneration',
            name='itinerydaywise',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='traveltriangle.ItineraryDayWise'),
        ),
    ]
