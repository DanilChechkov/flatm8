# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0009_auto_20210519_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='rmAgeL',
            field=models.DecimalField(verbose_name='Возраст соседа от:', default=18, max_digits=2, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rmAgeU',
            field=models.DecimalField(verbose_name='До:', default=18, max_digits=2, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rntPrice',
            field=models.DecimalField(verbose_name='Максимальная цена за всю квартиру:', default=18, max_digits=5, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rntSubway',
            field=models.CharField(verbose_name='Станция метро:', max_length=30, default='0', choices=[('Red', (('0', 'Девяткино'), ('1', 'Гражданский проспект'), ('2', 'Академическая'))), ('Blue', (('0', 'Озерки'), ('1', 'Проспект просвещения')))]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='rntTime',
            field=models.CharField(verbose_name='Срок аренды:', max_length=15, default='lgTerm', choices=[('shTerm', 'Не длительный'), ('lgTerm', 'Продолжительный')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='urAge',
            field=models.DecimalField(verbose_name='Ваш возраст:', default=18, max_digits=2, decimal_places=0),
        ),
    ]
