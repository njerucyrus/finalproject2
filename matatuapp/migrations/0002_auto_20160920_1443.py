# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 11:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matatuapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='departing_time',
            field=models.TimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='is_departed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='is_online',
            field=models.BooleanField(default=False),
        ),
    ]
