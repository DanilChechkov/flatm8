# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flmate', '0040_auto_20210525_1605'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.TextField(verbose_name='Сообщение')),
                ('pub_date', models.DateTimeField(verbose_name='Дата сообщения', default=django.utils.timezone.now)),
                ('is_readed', models.BooleanField(verbose_name='Прочитано', default=False)),
                ('author', models.ForeignKey(verbose_name='Пользователь', to=settings.AUTH_USER_MODEL)),
                ('chat', models.ForeignKey(verbose_name='Чат', to='flmate.Friend')),
            ],
        ),
    ]
