# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0003_auto_20150223_0106'),
    ]

    operations = [
        migrations.RenameField(
            model_name='supplier',
            old_name='supplier_id',
            new_name='supplier_idn',
        ),
    ]
