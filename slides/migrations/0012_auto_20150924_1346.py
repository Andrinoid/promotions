# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0011_slide_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]
