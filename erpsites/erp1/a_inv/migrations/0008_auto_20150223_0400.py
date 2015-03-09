# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0007_auto_20150223_0358'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(max_length=200, verbose_name=b'Address Line 1'),
            preserve_default=True,
        ),
    ]
