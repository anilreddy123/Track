# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0004_auto_20160806_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilereg',
            name='device_id',
            field=models.CharField(max_length=8, null=True),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='mobile_id',
            field=models.CharField(default=0, max_length=3, blank=True),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='mobile_no',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
