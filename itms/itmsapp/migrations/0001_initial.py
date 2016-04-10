# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-03 13:55
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bare_metal_servers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('storage_capacity', models.CharField(max_length=200, null=True)),
                ('cpus', models.IntegerField(default=1)),
                ('ram', models.CharField(max_length=200, null=True)),
                ('location', models.CharField(max_length=200, null=True)),
                ('other_info', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Servers',
            },
        ),
        migrations.CreateModel(
            name='cloud_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('other_info', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Cloud Type',
            },
        ),
        migrations.CreateModel(
            name='clouds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('other_info', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Clouds',
            },
        ),
        migrations.CreateModel(
            name='managers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Managers',
            },
        ),
        migrations.CreateModel(
            name='network_types',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('other_info', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Network_types',
            },
        ),
        migrations.CreateModel(
            name='networks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('range', models.CharField(max_length=200, null=True)),
                ('netmask', models.CharField(max_length=200, null=True)),
                ('dhcp_range', models.CharField(max_length=200, null=True)),
                ('other_info', models.CharField(max_length=200, null=True)),
                ('network_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.network_types')),
            ],
            options={
                'verbose_name_plural': 'Networks',
            },
        ),
        migrations.CreateModel(
            name='projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.managers')),
            ],
            options={
                'verbose_name_plural': 'Projects',
            },
        ),
        migrations.CreateModel(
            name='vms',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('username', models.CharField(max_length=200, null=True)),
                ('password', models.CharField(max_length=200, null=True)),
                ('assigned_to', models.CharField(max_length=200, null=True)),
                ('other_info', models.CharField(max_length=200, null=True)),
                ('cloud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.clouds')),
                ('network', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.networks')),
            ],
            options={
                'verbose_name_plural': 'VMs',
            },
        ),
        migrations.AddField(
            model_name='clouds',
            name='assigned_to_project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.projects'),
        ),
        migrations.AddField(
            model_name='clouds',
            name='cloud_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.cloud_types'),
        ),
        migrations.AddField(
            model_name='clouds',
            name='networks',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.networks'),
        ),
        migrations.AddField(
            model_name='clouds',
            name='nodes',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.bare_metal_servers'),
        ),
        migrations.AddField(
            model_name='bare_metal_servers',
            name='network',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='itmsapp.networks'),
        ),
    ]