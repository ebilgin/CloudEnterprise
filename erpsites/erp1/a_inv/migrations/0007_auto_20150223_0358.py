# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0006_auto_20150223_0316'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='line_1',
            field=models.CharField(max_length=200, verbose_name=b'Line 1'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(help_text=b'Apt., Suite etc.', max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
