# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-26 08:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0008_auto_20160926_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewforschooltrip',
            name='school_tour',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='schooltrips.SchoolTourDetail'),
        ),
    ]