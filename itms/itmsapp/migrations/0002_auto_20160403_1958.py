# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 19:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('itmsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networks',
            name='range',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
