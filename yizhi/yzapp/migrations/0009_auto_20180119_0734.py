# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-01-18 23:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yzapp', '0008_auto_20180106_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(default=False, verbose_name='published'),
        ),
        migrations.AlterField(
            model_name='image',
            name='img',
            field=models.FileField(upload_to=''),
        ),
    ]
