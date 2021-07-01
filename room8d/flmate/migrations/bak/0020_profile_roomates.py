# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0019_auto_20210520_1851'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.CharField(max_length=100, default='none', choices=[('none', 'none')]),
        ),
    ]
