# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-11-17 11:23
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0038_auto_20161117_1229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='itinerarydaywise',
            old_name='place_name_with_day',
            new_name='heading_day',
        ),
    ]