# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-15 07:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0059_auto_20161215_1256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdetail',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
