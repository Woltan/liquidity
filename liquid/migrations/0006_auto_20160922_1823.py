# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 16:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('liquid', '0005_auto_20160922_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='angestellter',
            name='Entlassungsdatum',
            field=models.DateField(blank=True, null=True),
        ),
    ]
