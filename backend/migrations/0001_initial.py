# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField()),
                ('time', models.IntegerField()),
                ('completed', models.IntegerField()),
            ],
            options={
                'ordering': ['time'],
                'get_latest_by': 'time',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('description', models.IntegerField()),
                ('completed', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'name',
            },
        ),
    ]
