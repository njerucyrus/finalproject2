# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 12:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('matatuapp', '0004_auto_20160920_1448'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='routes',
            options={'verbose_name_plural': 'Routes'},
        ),
        migrations.RenameField(
            model_name='travelling',
            old_name='depature_time',
            new_name='departure_time',
        ),
    ]
