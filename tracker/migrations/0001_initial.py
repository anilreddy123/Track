# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddDevice',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('device_id', models.CharField(max_length=8)),
                ('imei', models.CharField(max_length=15, null=True)),
                ('mobile_no', models.CharField(max_length=12)),
                ('ip', models.CharField(max_length=15)),
                ('port', models.CharField(max_length=5)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='MobileReg',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mobile_id', models.CharField(default=0, max_length=3, blank=True)),
                ('mobile_no', models.CharField(max_length=12)),
                ('device_id', models.CharField(max_length=8)),
                ('lat', models.FloatField(default=0.0)),
                ('lng', models.FloatField(default=0.0)),
                ('radius', models.CharField(max_length=5)),
                ('speed', models.CharField(max_length=3)),
            ],
        ),
    ]
