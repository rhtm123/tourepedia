# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-20 04:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_auto_20160918_1228'),
    ]

    operations = [
        migrations.CreateModel(
            name='HowToReach',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transpotation_type', models.CharField(choices=[('Himachal Pradesh', 'Himachal Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Sikkim', 'Sikkim'), ('Kashmir', 'Kashmir'), ('Meghalaya', 'Meghalaya')], max_length=128, null=True)),
                ('detail', models.TextField(max_length=100000, null=True)),
                ('placedetail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.PlaceDetail')),
            ],
        ),
    ]