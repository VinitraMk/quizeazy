# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-01 13:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_users_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(max_length=250),
        ),
    ]
