# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-17 08:11
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afterbook', '0003_bookedhotel_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookedhotel',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime.now, null=True),
        ),
    ]
