# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 12:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountholder',
            name='date_of_birth',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='accountholder',
            name='Acc_balance',
            field=models.DecimalField(decimal_places=2, default=5000, max_digits=20),
        ),
    ]
