# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-05 04:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0004_auto_20161004_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='calldetail',
            old_name='Comment',
            new_name='comment',
        ),
    ]
