# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-09 13:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0052_auto_20161209_1841'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='staff_name',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='tripdetail',
            name='staff_name',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
