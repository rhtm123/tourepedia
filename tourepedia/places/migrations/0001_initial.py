# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-01 09:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place_name', models.CharField(max_length=128, null=True)),
                ('place_tegline', models.CharField(max_length=256, null=True)),
                ('place_detail', models.TextField(max_length=100000, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='StateDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(choices=[('Himachal Pradesh', 'Himachal Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Sikkim', 'Sikkim'), ('Kashmir', 'Kashmir'), ('Meghalaya', 'Meghalaya')], max_length=128, null=True)),
                ('state_detail', models.TextField(max_length=100000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='placedetail',
            name='statedetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.StateDetail'),
        ),
    ]
