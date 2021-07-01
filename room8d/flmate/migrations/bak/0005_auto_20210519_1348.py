# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0004_remove_profile_date_of_birth'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rntSubway',
            field=models.CharField(max_length=30, default='0', choices=[(0, 'Девяткино'), (1, 'Гражданский проспект'), (2, 'Академическая')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='rntTime',
            field=models.CharField(max_length=15, default='lgTerm', choices=[('shTerm', 'Не длительный'), ('lgTerm', 'Продолжительный')]),
        ),
    ]
