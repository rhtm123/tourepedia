# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-25 08:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20160920_0933'),
        ('tours', '0006_tourdetail_number_days'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlacesInclude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placedetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='places.PlaceDetail')),
                ('tourdetail', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tours.TourDetail')),
            ],
        ),
    ]
