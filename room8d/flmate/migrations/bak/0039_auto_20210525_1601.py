# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flmate', '0038_auto_20210525_1551'),
    ]

    operations = [
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('prefs', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('subway', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('friend', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='profile',
            name='roomates',
        ),
        migrations.AddField(
            model_name='profile',
            name='roomates',
            field=models.ManyToManyField(to='flmate.Friend'),
        ),
    ]
