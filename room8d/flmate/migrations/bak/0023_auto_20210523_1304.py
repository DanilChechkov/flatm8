# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0022_auto_20210522_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='roomates',
            field=models.TextField(),
        ),
    ]
