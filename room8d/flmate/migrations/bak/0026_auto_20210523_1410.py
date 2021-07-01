# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0025_auto_20210523_1402'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.TextField(default=[]),
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
