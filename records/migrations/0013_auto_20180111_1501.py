# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-11 14:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0012_auto_20180111_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='_outstanding',
            field=models.IntegerField(db_column='Outstand', default=0),
        ),
    ]