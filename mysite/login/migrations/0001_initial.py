# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-03 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=140)),
                ('password', models.CharField(max_length=140)),
            ],
        ),
    ]
