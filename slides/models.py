# -*- coding: utf-8 -*-
from django.conf import settings
from django.db import models
from datetime import datetime


class Promotion(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nafn')
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    thumb = models.CharField(max_length=250, blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)
    is_active = models.BooleanField(default=False)
    in_private = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Slide(models.Model):
    promotion = models.ForeignKey(Promotion)
    date = models.DateTimeField(default=datetime.now, blank=True)
    image = models.CharField(max_length=400)
    thumb = models.CharField(max_length=400)
    headline = models.CharField(max_length=250, blank=True)
    sub_headline = models.CharField(max_length=250, blank=True)
    description = models.TextField(blank=True)
    html = models.TextField(blank=True)
    clean_html = models.TextField(blank=True)
    matrix = models.IntegerField(default=5)
    link = models.CharField(max_length=250, blank=True)
    is_active = models.BooleanField(default=True)
    index = models.IntegerField()

    def save(self, *args, **kwargs):
        ''' If this is the first slide. Save the thumb to the promnotion '''
        slides_count = Slide.objects.filter(promotion=self.promotion).count()
        if slides_count == 0:
            self.promotion.thumb = self.thumb
            self.promotion.save()
        super(Slide, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.promotion.name
