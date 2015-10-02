# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0014_slide_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='html',
            field=models.TextField(blank=True),
        ),
    ]
