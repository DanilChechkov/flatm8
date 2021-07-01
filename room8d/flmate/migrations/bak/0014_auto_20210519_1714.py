# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0013_auto_20210519_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rntSubway',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Станция метро:', max_length=30, default='0', choices=[('Red', (('0', 'Девяткино'), ('1', 'Гражданский проспект'), ('2', 'Академическая'))), ('Blue', (('3', 'Озерки'), ('4', 'Проспект просвещения')))]),
        ),
    ]
