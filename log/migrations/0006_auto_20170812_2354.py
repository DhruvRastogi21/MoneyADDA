# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 18:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_auto_20170812_2339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='credited_to',
            new_name='username_of_recipient',
        ),
    ]
