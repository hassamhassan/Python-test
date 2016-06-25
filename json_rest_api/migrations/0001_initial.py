# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-24 23:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('phone_number', models.CharField(max_length=20)),
                ('language', models.CharField(max_length=20)),
                ('currency', models.DateTimeField(max_length=20)),
            ],
        ),
    ]