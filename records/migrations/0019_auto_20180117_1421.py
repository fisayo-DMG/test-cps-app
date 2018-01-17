# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-17 13:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0018_auto_20180111_1529'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='name',
        ),
        migrations.AddField(
            model_name='student',
            name='other_names',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='student',
            name='surname',
            field=models.CharField(default=' ', max_length=20),
            preserve_default=False,
        ),
    ]
