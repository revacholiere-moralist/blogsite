# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20160107_2145'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='pub_house',
            field=models.TextField(default=''),
        ),
    ]