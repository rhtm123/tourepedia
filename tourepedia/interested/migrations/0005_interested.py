# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-24 03:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('interested', '0004_interestedforplace_placedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interested',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, null=True)),
                ('place', models.CharField(max_length=250, null=True)),
                ('email', models.CharField(max_length=250, null=True)),
                ('mobile', models.CharField(max_length=250, null=True)),
                ('date', models.DateField(blank=True)),
            ],
        ),
    ]
