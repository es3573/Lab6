# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-03-25 19:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='temp',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
    ]
