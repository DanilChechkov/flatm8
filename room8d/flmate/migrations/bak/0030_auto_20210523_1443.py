# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0029_auto_20210523_1419'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('uid', models.CharField(max_length=100)),
                ('prefs', models.DecimalField(max_digits=3, decimal_places=0)),
                ('hobbies', models.DecimalField(max_digits=3, decimal_places=0)),
                ('subway', models.DecimalField(max_digits=3, decimal_places=0)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='roomates',
            field=models.ForeignKey(to='flmate.Friend'),
        ),
    ]
