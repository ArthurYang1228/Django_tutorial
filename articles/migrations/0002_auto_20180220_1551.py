# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-02-20 07:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='location',
        ),
        migrations.RemoveField(
            model_name='post',
            name='photo',
        ),
    ]
