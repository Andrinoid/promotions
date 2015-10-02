# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0013_slide_index'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
