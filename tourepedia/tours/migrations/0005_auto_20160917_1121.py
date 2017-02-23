# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-09-17 05:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tours', '0004_tourdetail_term_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourdetail',
            name='statedetail',
        ),
        migrations.AlterField(
            model_name='tourcategory',
            name='category',
            field=models.CharField(choices=[('Nature', 'Nature'), ('Romantic', 'Romantic'), ('Family', 'Family'), ('Hill-Station', 'Hill-Station'), ('Adventure', 'Adventure'), ('Religious', 'religious'), ('Beaches', 'Beaches'), ('Wildlife', 'Wildlife')], max_length=128, null=True),
        ),
    ]
