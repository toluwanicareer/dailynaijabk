# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-14 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0011_bank'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='ref',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
