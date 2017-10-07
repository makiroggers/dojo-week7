# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-04 03:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20171004_0310'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='friend',
            name='last_name',
        ),
        migrations.AlterField(
            model_name='friendships',
            name='friend1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]