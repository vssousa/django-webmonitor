# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 13:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('monitoring_board', '0002_auto_20171209_1153'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='webid',
        ),
        migrations.RemoveField(
            model_name='page',
            name='webid',
        ),
    ]
