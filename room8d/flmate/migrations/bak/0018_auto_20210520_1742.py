# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0017_auto_20210520_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='abrCOMMUNISM',
            field=models.CharField(verbose_name='Отношение к быту:', max_length=30, default='idk', choices=[('capitalism', 'У каждого своя еда и посуда'), ('idk', 'Нечто среднее'), ('communism', 'Можно все общее')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='abrGUEST',
            field=models.CharField(verbose_name='Отношение к гостям:', max_length=25, default='hmguest', choices=[('noguest', 'Не люблю гостей'), ('hmguest', 'Нечто среднее'), ('siguest', 'Гости это обязательно')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='abrSOUL',
            field=models.CharField(verbose_name='Общий уровень шума:', max_length=25, default='midsou', choices=[('lowsou', 'Люблю тишину'), ('midsou', 'Нечто среднее'), ('nomsou', 'Уровень шума не главное')]),
        ),
    ]
