# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Type',
            fields=[
                ('address_type_code', models.CharField(max_length=10, serialize=False, primary_key=True)),
                ('address_type_description', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Addresses',
            fields=[
                ('address_id', models.AutoField(serialize=False, primary_key=True)),
                ('line_1', models.CharField(max_length=200)),
                ('line_2', models.CharField(max_length=200)),
                ('line_3', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
                ('country', models.CharField(max_length=200)),
                ('address_notes', models.CharField(max_length=200)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Supplier_Addresses',
            fields=[
                ('supplier_address_id', models.AutoField(serialize=False, primary_key=True)),
                ('supplier_address_notes', models.CharField(max_length=200)),
                ('address_id', models.ForeignKey(to='a_inv.Addresses')),
                ('address_type_code', models.ForeignKey(to='a_inv.Address_Type')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('supplier_id', models.AutoField(serialize=False, primary_key=True)),
                ('supplier_name', models.CharField(max_length=200)),
                ('supplier_notes', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='supplier_addresses',
            name='supplier_id',
            field=models.ForeignKey(to='a_inv.Suppliers'),
            preserve_default=True,
        ),
    ]
