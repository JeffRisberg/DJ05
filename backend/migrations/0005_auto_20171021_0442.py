# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_auto_20171020_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='time',
            field=models.TextField(),
        ),
    ]
