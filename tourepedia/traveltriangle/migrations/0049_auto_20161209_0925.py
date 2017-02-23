# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-09 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0048_remove_tripdetail_start_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripdetail',
            name='start_day',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='interested_status',
            field=models.CharField(choices=[('Not Interested', 'Not Interested'), ('Interested', 'Interested'), ('Highly Interested', 'Highly Interested'), ('Booked', 'Booked')], default='Interested', max_length=250, null=True),
        ),
    ]
