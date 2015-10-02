# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0005_auto_20150922_1337'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photo',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='image',
        ),
        migrations.RemoveField(
            model_name='slide',
            name='thumb',
        ),
    ]
