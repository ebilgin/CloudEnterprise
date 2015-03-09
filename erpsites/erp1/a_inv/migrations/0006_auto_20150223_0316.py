# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0005_auto_20150223_0311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='address_details',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='country',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='line_2',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='line_3',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='state',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address',
            name='zip_code',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='address_type',
            name='address_type_description',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplier',
            name='supplier_details',
            field=models.CharField(max_length=1000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='supplier_address',
            name='supplier_address_details',
            field=models.CharField(max_length=200, blank=True),
            preserve_default=True,
        ),
    ]
