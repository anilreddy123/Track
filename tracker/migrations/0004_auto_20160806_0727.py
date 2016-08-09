# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0003_auto_20160806_0725'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobilereg',
            name='ac_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='ac_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='ac_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='arrival_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='arrival_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='departure_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='departure_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='door_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='door_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='door_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='eng_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='eng_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='eng_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='fuel_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='fuel_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='fuel_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='radius_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='radius_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='speed_alert',
            field=models.NullBooleanField(default=False, choices=[(True, b'Alert ON'), (False, b'Dont Alert')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='speed_enable',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='speed_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='status_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'START'), (False, b'STOP')]),
        ),
        migrations.AddField(
            model_name='mobilereg',
            name='where_notify',
            field=models.NullBooleanField(default=False, choices=[(True, b'ON'), (False, b'OFF')]),
        ),
    ]
