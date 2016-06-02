# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('productid', models.IntegerField(default=0)),
                ('prodmodel', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('prodcolor', models.CharField(max_length=50)),
                ('prodsize', models.CharField(max_length=50)),
                ('prodprice', models.CharField(max_length=50)),
                ('cardtype', models.CharField(max_length=50)),
                ('cardnumber', models.IntegerField()),
                ('expiryyear', models.CharField(max_length=50)),
                ('expirymonth', models.CharField(max_length=50)),
                ('cvv', models.IntegerField()),
                ('cardname', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postalcode', models.IntegerField()),
                ('phonenumber', models.IntegerField()),
                ('email', models.CharField(max_length=50)),
                ('userid', models.IntegerField()),
                ('date', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='products',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('product', models.CharField(max_length=50)),
                ('model', models.CharField(max_length=50)),
                ('color', models.CharField(max_length=20)),
                ('size', models.CharField(max_length=20)),
                ('price', models.CharField(max_length=20)),
                ('details', models.TextField()),
                ('photo', models.ImageField(default='images/default.jpg', upload_to='media/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='userprofiles',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('userid', models.CharField(max_length=50)),
                ('dob', models.DateField(null=True)),
                ('country', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=50)),
                ('userphoto', models.ImageField(default='images/default.jpg', upload_to='media/')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
