# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-06 12:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fiteat', '0006_auto_20170906_1452'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='weight',
        ),
    ]
