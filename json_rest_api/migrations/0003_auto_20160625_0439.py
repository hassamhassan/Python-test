# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-25 04:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('json_rest_api', '0002_auto_20160625_0301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicearea',
            name='polygon',
            field=models.CharField(default='POLYGON ((0.0 0.0, 0.0 0.0, 0.0 0.0))', max_length=500),
        ),
    ]