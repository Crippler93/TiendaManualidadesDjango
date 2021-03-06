# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-09-14 18:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0002_auto_20160914_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='url_height',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='producto',
            name='url_width',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, height_field=models.PositiveIntegerField(default=20), upload_to='productos/%d/%m/%Y', width_field=models.PositiveIntegerField(default=20)),
        ),
    ]
