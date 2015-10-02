# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0006_auto_20150922_1646'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='slide',
            name='thumb',
            field=models.CharField(default=1, max_length=250),
            preserve_default=False,
        ),
    ]
