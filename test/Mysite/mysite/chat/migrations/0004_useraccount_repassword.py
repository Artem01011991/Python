# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-11-02 09:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_auto_20171101_2154'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='repassword',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
