# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0031_remove_profile_roomates'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.ForeignKey(default=0, to='flmate.Friend'),
        ),
    ]
