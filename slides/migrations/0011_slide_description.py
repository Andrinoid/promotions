# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0010_slide_matrix'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='description',
            field=models.TextField(default='hello'),
            preserve_default=False,
        ),
    ]
