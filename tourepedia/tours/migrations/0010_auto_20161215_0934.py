# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-15 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0009_auto_20161215_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourdetail',
            name='credit_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='credit_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourdetail',
            name='licence_type',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourimage',
            name='credit_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='tourimage',
            name='credit_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tourimage',
            name='licence_type',
            field=models.URLField(blank=True, null=True),
        ),
    ]
