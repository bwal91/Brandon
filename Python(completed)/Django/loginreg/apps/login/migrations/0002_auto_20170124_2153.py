# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-24 21:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email_add',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]