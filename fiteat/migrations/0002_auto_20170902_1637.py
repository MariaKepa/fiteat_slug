# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-02 14:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fiteat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('protein', models.FloatField(default=0.0)),
                ('carbon', models.FloatField(default=0.0)),
                ('fats', models.FloatField(default=0.0)),
                ('calories', models.FloatField(default=0.0)),
                ('weight', models.FloatField(default=100)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fiteat.Category')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AlterIndexTogether(
            name='product',
            index_together=set([('id', 'slug')]),
        ),
    ]