# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-22 16:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('records', '0026_auto_20180122_0233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='school_class',
            field=models.CharField(choices=[('CR', 'Creche'), ('PG1', 'Playgroup 1'), ('PG2', 'Playgroup 2'), ('KG1', 'Kindergarten 1'), ('KG2', 'Kindergarten 2'), ('GK', 'Grade K'), ('G1', 'Grade 1'), ('G2', 'Grade 2'), ('G3', 'Grade 3'), ('G4', 'Grade 4'), ('G5', 'Grade 5')], max_length=3),
        ),
    ]
