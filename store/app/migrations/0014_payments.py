# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_delete_payments'),
    ]

    operations = [
        migrations.CreateModel(
            name='payments',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('prodmodel', models.CharField(max_length=50)),
                ('productid', models.IntegerField(default=0)),
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
    ]
