# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-03 04:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0003_hotel_placedetail'),
    ]

    operations = [
        migrations.AddField(
            model_name='facilitytype',
            name='hotel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hotels.Hotel'),
        ),
    ]