# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 20:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_teamscore_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamscore',
            name='oppId',
            field=models.SmallIntegerField(db_index=True, default=0),
            preserve_default=False,
        ),
    ]