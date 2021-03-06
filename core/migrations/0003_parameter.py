# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-18 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20161117_1624'),
    ]

    operations = [
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('paypal_pct', models.DecimalField(decimal_places=3, max_digits=8)),
                ('paypal_fee', models.DecimalField(decimal_places=3, max_digits=8)),
                ('nexpay_pct', models.DecimalField(decimal_places=3, max_digits=8)),
                ('exchange_rate', models.DecimalField(decimal_places=3, max_digits=8)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('active_objects', django.db.models.manager.Manager()),
            ],
        ),
    ]
