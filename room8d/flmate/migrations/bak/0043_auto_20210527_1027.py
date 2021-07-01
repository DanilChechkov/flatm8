# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0042_auto_20210525_1821'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='friend',
            name='friend',
        ),
        migrations.AlterModelOptions(
            name='chatroom',
            options={'ordering': ['-cap']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
        migrations.DeleteModel(
            name='Friend',
        ),
    ]
