# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-05 22:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0015_property_thumbnail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shortlistedproperty',
            name='property',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shortlisted_property', to='properties.Property'),
        ),
        migrations.AlterField(
            model_name='shortlistedproperty',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='shortlisted_by_user', to=settings.AUTH_USER_MODEL),
        ),
    ]