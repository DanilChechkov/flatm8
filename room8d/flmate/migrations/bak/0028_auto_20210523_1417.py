# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0027_auto_20210523_1415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roomates',
            field=models.TextField(default='None'),
        ),
    ]
