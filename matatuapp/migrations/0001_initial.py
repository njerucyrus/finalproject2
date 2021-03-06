# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 05:19
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=50)),
                ('destination', models.CharField(max_length=50)),
                ('amount_paid', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Driver',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('national_id', models.PositiveIntegerField()),
                ('license', models.CharField(max_length=100, unique=True)),
                ('phone', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Passager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE')], max_length=10)),
                ('national_id', models.PositiveIntegerField()),
                ('age', models.PositiveIntegerField()),
                ('phone', models.CharField(max_length=13)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=128)),
                ('phone_no', models.CharField(max_length=13)),
                ('payment_mode', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=32)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Routes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=100, unique=True)),
                ('destination', models.CharField(max_length=100, unique=True)),
                ('fare', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Travelling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=128)),
                ('destination', models.CharField(max_length=128)),
                ('depature_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plate_no', models.CharField(max_length=20)),
                ('capacity', models.PositiveIntegerField()),
                ('vehicle_model', models.CharField(max_length=30)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matatuapp.Routes')),
            ],
        ),
        migrations.AddField(
            model_name='travelling',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matatuapp.Vehicle'),
        ),
        migrations.AddField(
            model_name='booking',
            name='passager',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matatuapp.Passager'),
        ),
        migrations.AddField(
            model_name='booking',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='matatuapp.Vehicle'),
        ),
    ]
