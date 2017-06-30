# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-04-21 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coosta_users', '0013_preapproveduser_documents'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='preapproveddocuments',
            name='user',
        ),
        migrations.AddField(
            model_name='preapproveddocuments',
            name='pre_approved_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pre_approved_user', to='coosta_users.PreApprovedUser'),
        ),
    ]