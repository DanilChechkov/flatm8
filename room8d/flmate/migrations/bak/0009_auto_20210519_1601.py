# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0008_auto_20210519_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='urAge',
            field=models.DecimalField(verbose_name='Ваш возраст', default=18, max_digits=2, decimal_places=0),
        ),
    ]
