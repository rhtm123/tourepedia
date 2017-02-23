# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-12-11 03:37
from __future__ import unicode_literals

from django.db import migrations, models
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20160920_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='placetovisit',
            name='attraction_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placetovisit',
            name='credit_name',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='placetovisit',
            name='credit_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placetovisit',
            name='licence_type',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='placetovisit',
            name='place_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='places'),
        ),
        migrations.AlterField(
            model_name='placedetail',
            name='place_tagline',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='statedetail',
            name='state_name',
            field=models.CharField(choices=[('Himachal Pradesh', 'Himachal Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Kerala', 'Kerala'), ('Rajasthan', 'Rajasthan'), ('Maharastra', 'Maharastra'), ('Jammu & Kashmir', 'Jammu & Kashmir'), ('West Bengal', 'West Bengal'), ('Sikkim', 'Sikkim'), ('Kashmir', 'Kashmir'), ('Meghalaya', 'Meghalaya')], max_length=128, null=True),
        ),
    ]