# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20171018_0037'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'ordering': ['time']},
        ),
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ['name']},
        ),
        migrations.AlterField(
            model_name='event',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='item',
            name='description',
            field=models.TextField(),
        ),
    ]
