# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0005_auto_20160806_0728'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=8)),
                ('mobile_no', models.CharField(max_length=12)),
                ('notify_type', models.IntegerField(max_length=3)),
                ('notify_result', models.CharField(max_length=80)),
            ],
        ),
    ]
