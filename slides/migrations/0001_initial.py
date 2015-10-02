# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Promotion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'Nafn')),
                ('thumb', models.CharField(max_length=250)),
                ('date', models.DateTimeField(default=datetime.datetime.now, blank=True)),
                ('is_active', models.BooleanField(default=False, verbose_name=b'Er deilt \xc3\xa1 vegg')),
                ('in_private', models.BooleanField(default=False, verbose_name=b'Er \xc3\xad vinnslu')),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.FileField(upload_to=b'documents/%Y/%m/%d')),
                ('headline', models.CharField(max_length=250)),
                ('sub_headline', models.CharField(max_length=250)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
    ]
