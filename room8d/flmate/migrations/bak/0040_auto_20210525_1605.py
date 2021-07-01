# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('flmate', '0039_auto_20210525_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='friend',
            name='friend',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
