# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-03 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fiteat', '0002_auto_20170902_1637'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='pathtopicture',
        ),
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='fotocategory/%Y/%m/%d'),
        ),
    ]
