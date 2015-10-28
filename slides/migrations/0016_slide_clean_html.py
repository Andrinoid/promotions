# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0015_slide_html'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='clean_html',
            field=models.TextField(blank=True),
        ),
    ]
