# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0032_profile_roomates'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.ManyToManyField(to='flmate.Friend'),
        ),
    ]
