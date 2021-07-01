# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0006_auto_20210519_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rmAgeL',
            field=models.DecimalField(default=18, max_digits=2, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rmAgeU',
            field=models.DecimalField(default=18, max_digits=2, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rntPrice',
            field=models.DecimalField(default=18, max_digits=5, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='urAge',
            field=models.DecimalField(default=18, max_digits=2, decimal_places=0),
        ),
    ]
