# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-26 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0014_auto_20161226_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='thumbnail',
            field=models.TextField(blank=True, null=True),
        ),
    ]
