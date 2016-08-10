# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0011_usertype'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usertype',
            options={'permissions': (('add_user', 'Add User'),)},
        ),
        migrations.RenameField(
            model_name='usertype',
            old_name='Reseller',
            new_name='reseller',
        ),
    ]
