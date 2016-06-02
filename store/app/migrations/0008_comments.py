# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_delete_comments'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('productid', models.IntegerField(default=0)),
                ('username', models.CharField(max_length=50)),
                ('userid', models.IntegerField(default=0)),
                ('comment', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
