# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 16:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0012_property_search_index'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='listed_on',
            field=models.DateField(auto_created=True, blank=True, null=True),
        ),
    ]
