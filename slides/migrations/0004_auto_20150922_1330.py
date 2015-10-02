# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slides', '0003_auto_20150921_1524'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(default=None, null=True, upload_to=b'/Users/andri/piparJobs/Sites/promos/media/photos/%Y/%m/%d/', blank=True)),
                ('filename', models.CharField(max_length=60, null=True, blank=True)),
            ],
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
