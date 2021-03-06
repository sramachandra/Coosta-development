# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-17 14:50
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
            name='Property',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zip_code', models.CharField(max_length=15)),
                ('home_type', models.CharField(max_length=20)),
                ('beds', models.IntegerField()),
                ('property_value', models.IntegerField()),
                ('baths', models.IntegerField(default=1)),
                ('rooms', models.IntegerField()),
                ('property_size', models.IntegerField()),
                ('floors', models.IntegerField(default=0)),
                ('roof', models.BooleanField(default=False)),
                ('basement', models.CharField(max_length=5)),
                ('year_built', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('other_features', models.TextField()),
                ('status', models.BooleanField(default=True)),
                ('latitude', models.CharField(max_length=50)),
                ('longitude', models.CharField(max_length=50)),
                ('year_renovated', models.CharField(max_length=10)),
                ('car_park', models.CharField(max_length=10)),
            ],
            options={
                'verbose_name_plural': 'Property',
            },
        ),
        migrations.CreateModel(
            name='PropertyImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='C:\\Users\\Avinash.Mallik\\Documents\\repos\\Coosta\\coosta/static/uploads')),
            ],
            options={
                'verbose_name_plural': 'Property Images',
            },
        ),
        migrations.AddField(
            model_name='property',
            name='images',
            field=models.ManyToManyField(to='properties.PropertyImages'),
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
