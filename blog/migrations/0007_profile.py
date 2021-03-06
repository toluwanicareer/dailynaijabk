# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-09-19 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0006_auto_20170914_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, max_length=500)),
                ('location', models.CharField(blank=True, max_length=30)),
                ('country', models.CharField(blank=True, max_length=30)),
                ('post_pic', models.ImageField(blank=True, null=True, upload_to=b'media')),
                ('cover_pic', models.ImageField(blank=True, null=True, upload_to=b'media')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
