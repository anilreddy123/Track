# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0006_notify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='notify_type',
            field=models.IntegerField(),
        ),
    ]
