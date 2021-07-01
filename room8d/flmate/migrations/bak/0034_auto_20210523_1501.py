# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0033_auto_20210523_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='friend',
            name='fid',
            field=models.CharField(max_length=100, default='none'),
        ),
        migrations.AlterField(
            model_name='friend',
            name='hobbies',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='friend',
            name='prefs',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='friend',
            name='subway',
            field=models.DecimalField(default=0, max_digits=3, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='friend',
            name='uid',
            field=models.CharField(max_length=100, default='none'),
        ),
    ]
