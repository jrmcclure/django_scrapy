# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 21:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20170824_2142'),
    ]

    operations = [
        migrations.AddField(
            model_name='teamscore',
            name='final',
            field=models.BooleanField(default=False),
        ),
    ]
