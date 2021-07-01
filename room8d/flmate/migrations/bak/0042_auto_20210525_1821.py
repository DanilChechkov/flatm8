# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flmate', '0041_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Chatroom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('cap', models.DecimalField(default=0, max_digits=3, decimal_places=0)),
                ('sub', models.DecimalField(default=0, max_digits=1, decimal_places=0)),
                ('members', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['pub_date']},
        ),
        migrations.AlterField(
            model_name='message',
            name='chat',
            field=models.ForeignKey(verbose_name='Чат', to='flmate.Chatroom'),
        ),
    ]
