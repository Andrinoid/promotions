# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0004_auto_20150922_1330'),
    ]

    operations = [
        migrations.AddField(
            model_name='slide',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'/Users/andri/piparJobs/Sites/promos/media/images/%Y/%m/%d/', blank=True),
        ),
        migrations.AddField(
            model_name='slide',
            name='thumb',
            field=models.ImageField(default=None, null=True, upload_to=b'/Users/andri/piparJobs/Sites/promos/media/thumbs/%Y/%m/%d/', blank=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=b'/Users/andri/piparJobs/Sites/promos/media/images/%Y/%m/%d/', blank=True),
        ),
    ]
