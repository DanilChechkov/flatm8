# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0018_auto_20210520_1742'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='aprFRETM',
            field=multiselectfield.db.fields.MultiSelectField(verbose_name='Как проводишь свободное время:', max_length=50, default='imprusf', choices=[('cafe', 'Кафе'), ('socnet', 'Соц.сети'), ('drinkin', 'Выпивка'), ('cinema', 'Кинотеатр'), ('culture', 'Культурные места: театры, выставки, музеи и т.д'), ('reading', 'Чтение'), ('activity', 'Активный отдых'), ('imprusf', 'Развитие себя'), ('games', 'Игры'), ('study', 'Учеба')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprPETS',
            field=models.CharField(verbose_name='Питомцы допустимы?', max_length=15, default='nomater', choices=[('si', 'Да'), ('nomater', 'Мне без разницы'), ('no', 'Нет')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprR8GEN',
            field=models.CharField(verbose_name='Пол соседа:', max_length=15, default='inbetween', choices=[('man', 'Мужской'), ('inbetween', 'Нечто среднее'), ('woman', 'Женский')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprR8RELIGY',
            field=models.CharField(verbose_name='Религия соседа:', max_length=25, default='pastafarian', choices=[('сhrist', 'Христианство'), ('muslim', 'Ислам'), ('induism', 'Индуизм'), ('budism', 'Будизм'), ('iudaism', 'Иудаизм'), ('pastafarian', 'Пастафарианство'), ('ateism', 'Я считаю себя атеистом'), ('nosing', 'Это не имеет значения')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprSEXUAL',
            field=models.CharField(verbose_name='Твоя сексуальная ориентация:', max_length=10, default='bi', choices=[('hetero', 'Гетеро'), ('bi', 'Би'), ('Homo', 'Гомо')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprTELLUS',
            field=models.TextField(verbose_name='Пара слов о тебе(250 символов):', max_length=250, default='Мне было лень это менять.'),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprUGEN',
            field=models.CharField(verbose_name='Твой пол:', max_length=15, default='inbetween', choices=[('man', 'Мужской'), ('inbetween', 'Нечто среднее'), ('woman', 'Женский')]),
        ),
        migrations.AddField(
            model_name='profile',
            name='aprURRELIGY',
            field=models.CharField(verbose_name='Религия:', max_length=25, default='pastafarian', choices=[('сhrist', 'Христианство'), ('muslim', 'Ислам'), ('induism', 'Индуизм'), ('budism', 'Будизм'), ('iudaism', 'Иудаизм'), ('pastafarian', 'Пастафарианство'), ('ateism', 'Я считаю себя атеистом'), ('nosing', 'Это не имеет значения')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='photo',
            field=models.ImageField(verbose_name='Тут можно загрузить свое фото', blank=True, upload_to='users/%Y/%m/%d'),
        ),
    ]
