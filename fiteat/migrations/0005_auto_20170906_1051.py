# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 08:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiteat', '0004_auto_20170905_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='protein',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
