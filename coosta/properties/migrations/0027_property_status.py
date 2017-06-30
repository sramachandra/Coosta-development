# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-14 07:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0026_remove_property_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.ForeignKey(blank=True, default=1, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='property_status', to='properties.PropertyStatus'),
        ),
    ]
