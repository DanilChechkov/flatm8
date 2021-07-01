# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0007_auto_20210519_1527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rntSubway',
            field=models.CharField(max_length=30, default='0', choices=[('Red', (('0', 'Девяткино'), ('1', 'Гражданский проспект'), ('2', 'Академическая'))), ('Blue', (('0', 'Озерки'), ('1', 'Проспект просвещения')))]),
        ),
    ]
