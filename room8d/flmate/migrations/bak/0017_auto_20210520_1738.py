# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0016_auto_20210520_1702'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='abrCLEAN',
            field=models.DecimalField(verbose_name='Сколько раз в месяц проводишь уборку(0-30):', default=8, max_digits=2, decimal_places=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='abrCOMMUNISM',
            field=models.CharField(verbose_name='Отношение к быту:', max_length=30, default='capitalism', choices=[('capitalism', 'У каждого своя еда и посуда'), ('communism', 'Можно все общее')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='abrGUEST',
            field=models.CharField(verbose_name='Отношение к гостям:', max_length=25, default='noguest', choices=[('noguest', 'Не люблю гостей'), ('siguest', 'Гости это обязательно')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='abrSOUL',
            field=models.CharField(verbose_name='Общий уровень шума:', max_length=25, default='lowsou', choices=[('lowsou', 'Люблю тишину'), ('nomsou', 'Уровень шума не главное')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='abrTEMP',
            field=models.DecimalField(verbose_name='Комфортная температура(12-28):', default=24, max_digits=2, decimal_places=0),
        ),
    ]
