# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-03 05:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_agenda_tanggal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agenda',
            name='tanggal',
            field=models.DateField(null=True),
        ),
    ]