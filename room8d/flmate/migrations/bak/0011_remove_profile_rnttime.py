# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0010_auto_20210519_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='rntTime',
        ),
    ]
