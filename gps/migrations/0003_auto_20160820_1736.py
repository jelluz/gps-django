# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-20 15:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gps', '0002_gps_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gps',
            name='timestamp',
            field=models.TimeField(auto_now=True, verbose_name='timestamp'),
        ),
    ]