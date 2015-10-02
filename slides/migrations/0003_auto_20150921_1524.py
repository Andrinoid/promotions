# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0002_slide_promotion'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='date',
            field=models.DateTimeField(default=datetime.datetime.now, blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='thumb',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='promotion',
            name='in_private',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='promotion',
            name='thumb',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.CharField(max_length=250),
        ),
    ]
