# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0007_auto_20150922_1646'),
    ]

    operations = [
        migrations.AlterField(
            model_name='slide',
            name='headline',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='link',
            field=models.CharField(max_length=250, blank=True),
        ),
        migrations.AlterField(
            model_name='slide',
            name='sub_headline',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]
