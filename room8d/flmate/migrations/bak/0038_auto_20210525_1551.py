# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0037_auto_20210523_1706'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.CharField(max_length=25, default='def'),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
