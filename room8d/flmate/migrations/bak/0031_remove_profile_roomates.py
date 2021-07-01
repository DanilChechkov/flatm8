# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0030_auto_20210523_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
    ]
