# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0020_profile_roomates'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='rntPrice',
            new_name='rntUPrice',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='aprSEXUAL',
        ),
        migrations.AddField(
            model_name='profile',
            name='rntLPrice',
            field=models.DecimalField(verbose_name='Минимальная цена за всю квартиру:', default=10000, max_digits=5, decimal_places=0),
        ),
        migrations.AlterField(
            model_name='profile',
            name='aprR8GEN',
            field=models.CharField(verbose_name='Пол соседа:', max_length=20, default='inbetween', choices=[('man', 'Мужской'), ('inbetween', 'Не имеет значения'), ('woman', 'Женский')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='aprUGEN',
            field=models.CharField(verbose_name='Твой пол:', max_length=20, default='inbetween', choices=[('man', 'Мужской'), ('inbetween', 'Не имеет значения'), ('woman', 'Женский')]),
        ),
    ]
