# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-05 12:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiteat', '0003_auto_20170903_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='weight',
            field=models.DecimalField(decimal_places=3, max_digits=10),
        ),
    ]