# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-20 06:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0005_auto_20160917_1121'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetail',
            name='number_days',
            field=models.IntegerField(null=True),
        ),
    ]