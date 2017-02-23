# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-17 06:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afterbook', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookedhotel',
            name='room_price',
        ),
        migrations.AddField(
            model_name='bookedhotel',
            name='room_numbers',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookedhotel',
            name='total_price',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='bookedhotel',
            name='trip_nights',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]