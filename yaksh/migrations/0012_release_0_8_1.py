# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-18 06:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0011_release_0_8_0'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestatus',
            name='percent_completed',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='time_between_attempts',
            field=models.FloatField(default=0.0, verbose_name='Time Between Quiz Attempts in hours'),
        ),
    ]
