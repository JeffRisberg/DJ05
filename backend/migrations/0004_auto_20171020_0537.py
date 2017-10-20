# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20171018_0102'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 5, 37, 3, 988408, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 5, 37, 12, 108532, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 5, 37, 29, 284190, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='last_updated',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 20, 5, 37, 35, 820471, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]
