# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-07-11 10:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0006_auto_20190711_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consumption',
            name='date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
