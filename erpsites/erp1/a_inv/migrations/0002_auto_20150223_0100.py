# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('a_inv', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier_Address',
            fields=[
                ('supplier_address_id', models.AutoField(serialize=False, primary_key=True)),
                ('supplier_address_notes', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RenameModel(
            old_name='Addresses',
            new_name='Address',
        ),
        migrations.RenameModel(
            old_name='Suppliers',
            new_name='Supplier',
        ),
        migrations.RemoveField(
            model_name='supplier_addresses',
            name='address_id',
        ),
        migrations.RemoveField(
            model_name='supplier_addresses',
            name='address_type_code',
        ),
        migrations.RemoveField(
            model_name='supplier_addresses',
            name='supplier_id',
        ),
        migrations.DeleteModel(
            name='Supplier_Addresses',
        ),
        migrations.AddField(
            model_name='supplier_address',
            name='address_id',
            field=models.ForeignKey(to='a_inv.Address'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier_address',
            name='address_type_code',
            field=models.ForeignKey(to='a_inv.Address_Type'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='supplier_address',
            name='supplier_id',
            field=models.ForeignKey(to='a_inv.Supplier'),
            preserve_default=True,
        ),
    ]
