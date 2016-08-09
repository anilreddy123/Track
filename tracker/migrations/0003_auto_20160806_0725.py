# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0002_auto_20160806_0724'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mobilereg',
            name='ac_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='ac_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='ac_notify',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='arrival_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='arrival_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='departure_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='departure_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='device_id',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='door_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='door_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='door_notify',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='eng_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='eng_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='eng_notify',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='fuel_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='fuel_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='fuel_notify',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='mobile_id',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='mobile_no',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='radius_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='radius_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='speed_alert',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='speed_enable',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='speed_notify',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='status_notify',
        ),
        migrations.RemoveField(
            model_name='mobilereg',
            name='where_notify',
        ),
    ]
