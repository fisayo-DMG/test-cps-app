# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-11 14:09
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0014_auto_20180111_1503'),
    ]

    operations = [
        migrations.RenameField(
            model_name='payment',
            old_name='_Outstanding',
            new_name='outstanding',
        ),
    ]
