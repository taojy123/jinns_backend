# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-26 06:23
from __future__ import unicode_literals

from django.db import migrations, models
import jinns.utils


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20180403_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='token',
            field=models.CharField(default=jinns.utils.make_token, max_length=255),
        ),
    ]
