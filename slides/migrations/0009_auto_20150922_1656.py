# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0008_auto_20150922_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='image',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='slide',
            name='thumb',
            field=models.CharField(max_length=400),
        ),
    ]
