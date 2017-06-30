# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 18:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0010_auto_20161122_2353'),
    ]

    operations = [
        migrations.AlterField(
            model_name='propertyimages',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prop_img', to='properties.Images'),
        ),
        migrations.AlterField(
            model_name='propertyimages',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prop_prop', to='properties.Property'),
        ),
    ]