# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-22 17:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_registration', '0003_auto_20170922_1139'),
        ('review_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='login_registration.User'),
            preserve_default=False,
        ),
    ]