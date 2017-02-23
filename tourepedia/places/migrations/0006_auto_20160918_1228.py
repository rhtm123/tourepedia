# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-18 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0005_placedetail_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlaceImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='places')),
            ],
        ),
        migrations.RenameModel(
            old_name='MustDo',
            new_name='ImpPoint',
        ),
        migrations.AddField(
            model_name='placedetail',
            name='main_img',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='places'),
        ),
        migrations.AddField(
            model_name='placeimage',
            name='placedetail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='places.PlaceDetail'),
        ),
    ]