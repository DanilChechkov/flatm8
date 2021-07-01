# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0035_remove_friend_uid'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='friend',
            options={'ordering': ('-fid',)},
        ),
    ]
