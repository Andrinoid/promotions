# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0012_auto_20150924_1346'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='index',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
