# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='promotion',
            field=models.ForeignKey(default=1, to='slides.Promotion'),
            preserve_default=False,
        ),
    ]
