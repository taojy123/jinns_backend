# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-03 06:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CouponCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metafield', jsonfield.fields.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('coupon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Coupon')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('metafield', jsonfield.fields.JSONField(default=dict)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('full_name', models.CharField(blank=True, max_length=255)),
                ('mobile', models.CharField(blank=True, max_length=255)),
                ('balance', models.FloatField(default=0, help_text='账户余额')),
                ('openid', models.CharField(blank=True, max_length=255)),
                ('nickname', models.CharField(blank=True, max_length=255)),
                ('headimgurl', models.CharField(blank=True, max_length=255)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Shop')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='couponcode',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.Customer'),
        ),
    ]
