# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0002_auto_20150223_0100'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier_address',
            old_name='address_id',
            new_name='add_id',
        ),
        migrations.RenameField(
            model_name='supplier_address',
            old_name='supplier_id',
            new_name='supp_id',
        ),
    ]
