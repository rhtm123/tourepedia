# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-11 11:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0020_hotelprice_extra_person_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='city',
            field=models.CharField(blank=True, max_length=240, null=True),
        ),
    ]
