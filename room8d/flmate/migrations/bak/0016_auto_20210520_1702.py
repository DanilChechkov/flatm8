# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0015_auto_20210520_1700'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='abuORGL',
            field=models.DecimalField(verbose_name='Уровень вашей организованности(0-99):', default=50, max_digits=2, decimal_places=0),
        ),
    ]
