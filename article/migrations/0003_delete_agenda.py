# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 05:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20160103_1229'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Agenda',
        ),
    ]
