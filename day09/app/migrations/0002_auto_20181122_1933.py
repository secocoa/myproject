# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-22 11:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uage',
            field=models.IntegerField(default=20),
        ),
    ]