# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-12 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0023_auto_20170306_1815'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Property status',
            },
        ),
    ]
