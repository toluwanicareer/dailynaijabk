# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-20 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20170919_1547'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='facebook_link',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='instagram_link',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='linkedin_link',
            field=models.URLField(blank=True, max_length=50, null=True),
        ),
    ]
