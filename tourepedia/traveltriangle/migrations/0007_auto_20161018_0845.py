# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-10-18 03:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('traveltriangle', '0006_itinerarydaywise_quote_quotegeneration'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerarydaywise',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='traveltriangle.Quote'),
        ),
        migrations.AddField(
            model_name='quotegeneration',
            name='quote',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='traveltriangle.Quote'),
        ),
    ]