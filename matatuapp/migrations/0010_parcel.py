# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-20 20:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matatuapp', '0009_booking_date_booked'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parcel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_full_name', models.CharField(max_length=128)),
                ('owner_phone_no', models.CharField(max_length=13)),
                ('owner_national_id', models.PositiveIntegerField()),
                ('receiver_phone_no', models.CharField(max_length=13)),
                ('receiver_national_id', models.PositiveIntegerField()),
                ('parcel_description', models.TextField(max_length=140)),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
            ],
        ),
    ]
