# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.TextField()),
                ('value', models.IntegerField()),
                ('description', models.IntegerField()),
                ('completed', models.IntegerField()),
            ],
            options={
                'ordering': ['name'],
                'get_latest_by': 'name',
            },
        ),
        migrations.RenameModel(
            old_name='Events',
            new_name='Event',
        ),
        migrations.DeleteModel(
            name='Items',
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['text'], 'get_latest_by': 'text'},
        ),
    ]
