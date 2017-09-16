# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-09-16 14:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20170914_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='role',
            field=models.CharField(choices=[('Advertiser', 'Advertiser'), ('Content Writer', 'Content Writer'), ('Social Media Executives', 'Social Media Executives')], default='Content Writer', max_length=50, null=True),
        ),
    ]
