# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-27 07:20
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mall', '0003_auto_20180418_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderproduct',
            name='order',
        ),
        migrations.RemoveField(
            model_name='orderproduct',
            name='product',
        ),
        migrations.DeleteModel(
            name='OrderProduct',
        ),
    ]
