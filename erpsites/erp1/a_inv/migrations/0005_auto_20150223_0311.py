# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0004_auto_20150223_0109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='address_notes',
            new_name='address_details',
        ),
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_notes',
            new_name='supplier_details',
        ),
        migrations.RenameField(
            model_name='supplier_address',
            old_name='add_id',
            new_name='address_id',
        ),
        migrations.RenameField(
            model_name='supplier_address',
            old_name='supplier_address_notes',
            new_name='supplier_address_details',
        ),
        migrations.RenameField(
            model_name='supplier_address',
            old_name='supp_id',
            new_name='supplier_id',
        ),
    ]
