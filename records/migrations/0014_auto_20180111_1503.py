# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-11 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0013_auto_20180111_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='payment',
            name='_outstanding',
        ),
        migrations.AddField(
            model_name='payment',
            name='_Outstanding',
            field=models.IntegerField(default=0),
        ),
    ]
