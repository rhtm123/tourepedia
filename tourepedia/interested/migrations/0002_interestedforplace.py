# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-06 08:53
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20160920_0933'),
        ('interested', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterestedForPlace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('name', models.CharField(max_length=1024, null=True)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('mobile', models.CharField(max_length=12, null=True)),
                ('place', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.PlaceDetail')),
            ],
        ),
    ]
