# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0023_auto_20210523_1304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friends',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=100)),
                ('prefs', models.DecimalField(max_digits=3, decimal_places=0)),
                ('hobbies', models.DecimalField(max_digits=3, decimal_places=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.ManyToManyField(to='flmate.Friends'),
        ),
    ]
