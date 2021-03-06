# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-24 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('abbv', models.CharField(db_index=True, max_length=16)),
                ('teamId', models.SmallIntegerField(db_index=True)),
                ('week', models.SmallIntegerField(db_index=True)),
                ('tmTotalPts', models.FloatField(default=0.0, null=True)),
                ('team_ytp', models.SmallIntegerField(null=True)),
                ('team_ip', models.SmallIntegerField(null=True)),
                ('team_pmr', models.SmallIntegerField(null=True)),
                ('team_liveproj', models.FloatField(default=0.0, null=True)),
            ],
        ),
    ]
