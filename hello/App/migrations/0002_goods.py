# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2018-11-14 10:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goodname', models.CharField(max_length=20)),
                ('userid', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='App.User')),
            ],
        ),
    ]
