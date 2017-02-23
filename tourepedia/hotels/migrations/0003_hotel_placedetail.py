# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 04:20
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
        ('hotels', '0002_auto_20160902_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='placedetail',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.PlaceDetail'),
        ),
    ]
