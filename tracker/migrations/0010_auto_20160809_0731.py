# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0009_auto_20160809_0717'),
    ]

    operations = [
        migrations.CreateModel(
            name='IP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ip', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('port_no', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='adddevice',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='adddevice',
            name='ip',
            field=models.ForeignKey(to='tracker.IP', null=True),
        ),
        migrations.AlterField(
            model_name='adddevice',
            name='port',
            field=models.ForeignKey(to='tracker.Port', null=True),
        ),
    ]
