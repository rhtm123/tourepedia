# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-26 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_auto_20160926_1341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewforschooltrip',
            name='review_text',
            field=models.TextField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='reviewforschooltrip',
            name='school_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='reviewfortours',
            name='review_text',
            field=models.TextField(max_length=1000, null=True),
        ),
    ]
