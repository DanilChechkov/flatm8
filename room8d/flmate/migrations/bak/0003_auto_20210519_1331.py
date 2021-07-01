# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('flmate', '0002_auto_20210517_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('urAge', models.DecimalField(max_digits=2, decimal_places=0)),
                ('rmAgeL', models.DecimalField(max_digits=2, decimal_places=0)),
                ('rmAgeU', models.DecimalField(max_digits=2, decimal_places=0)),
                ('rntPrice', models.DecimalField(max_digits=5, decimal_places=0)),
                ('photo', models.ImageField(blank=True, upload_to='users/%Y/%m/%d')),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
