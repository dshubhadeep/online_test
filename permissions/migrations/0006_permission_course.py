# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-05-30 11:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('yaksh', '0015_release_0_10_0'),
        ('permissions', '0005_team_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='permission',
            name='course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='yaksh.Course'),
        ),
    ]
