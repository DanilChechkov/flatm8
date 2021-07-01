# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0034_auto_20210523_1501'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='uid',
        ),
    ]
