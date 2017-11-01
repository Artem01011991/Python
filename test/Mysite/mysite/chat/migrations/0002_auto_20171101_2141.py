# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-01 18:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='nick_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='useraccount',
            name='second_name',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='password',
            field=models.CharField(max_length=100),
        ),
    ]
