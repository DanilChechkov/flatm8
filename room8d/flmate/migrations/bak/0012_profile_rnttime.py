# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0011_remove_profile_rnttime'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='rntTime',
            field=models.CharField(verbose_name='Срок аренды:', max_length=15, default='lgTerm', choices=[('shTerm', 'Не длительный'), ('lgTerm', 'Продолжительный')]),
        ),
    ]
