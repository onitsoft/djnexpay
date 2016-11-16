# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-15 20:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=15)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted', models.BooleanField(default=False)),
                ('disabled', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
                ('order_number', models.CharField(max_length=10, unique=True)),
                ('amount_gross', models.DecimalField(decimal_places=2, max_digits=12)),
                ('comission', models.DecimalField(decimal_places=2, max_digits=12)),
                ('amount_net', models.DecimalField(decimal_places=2, max_digits=12)),
                ('cbu_number', models.CharField(max_length=20)),
                ('account_number', models.CharField(max_length=15)),
                ('account_owner', models.CharField(max_length=20)),
                ('account_owner_dni', models.CharField(max_length=12)),
                ('paypal_email', models.CharField(max_length=50)),
                ('tracking_email', models.CharField(max_length=50)),
                ('is_paid', models.BooleanField(default=False)),
                ('is_released', models.BooleanField(default=False)),
                ('is_completed', models.BooleanField(default=False)),
                ('is_failed', models.BooleanField(default=False)),
                ('bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Bank')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]