# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-02 06:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='detail',
            old_name='img_credit',
            new_name='img_credit_name',
        ),
        migrations.AddField(
            model_name='detail',
            name='license_type',
            field=models.URLField(blank=True, null=True),
        ),
    ]
