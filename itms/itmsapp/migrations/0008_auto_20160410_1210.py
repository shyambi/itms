# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-10 12:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('itmsapp', '0007_clouds_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='device_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Device Types',
            },
        ),
        migrations.CreateModel(
            name='devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=200)),
                ('other_info', models.CharField(blank=True, max_length=200, null=True)),
                ('assigned_to', models.CharField(blank=True, max_length=200, null=True)),
                ('device_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='itmsapp.device_types')),
            ],
            options={
                'verbose_name_plural': 'Device Types',
            },
        ),
        migrations.AlterModelOptions(
            name='cloud_types',
            options={'verbose_name_plural': 'Cloud Types'},
        ),
    ]
