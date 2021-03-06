# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-21 13:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('afterbook', '0007_auto_20161220_1306'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedtravel',
            name='flight_ticket1',
            field=models.FileField(blank=True, null=True, upload_to='traveltriangle/flight'),
        ),
        migrations.AddField(
            model_name='bookedtravel',
            name='flight_ticket2',
            field=models.FileField(blank=True, null=True, upload_to='traveltriangle/flight'),
        ),
        migrations.AddField(
            model_name='bookedtravel',
            name='train_ticket1',
            field=models.FileField(blank=True, null=True, upload_to='traveltriangle/train'),
        ),
        migrations.AddField(
            model_name='bookedtravel',
            name='train_ticket2',
            field=models.FileField(blank=True, null=True, upload_to='traveltriangle/train'),
        ),
        migrations.AddField(
            model_name='otherbooking',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='traveltriangle/other'),
        ),
        migrations.AlterField(
            model_name='bookedhotel',
            name='price_paid',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
