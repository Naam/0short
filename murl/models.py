#-*- coding: utf-8 -*-
from django.db import models
from django import forms
import string
import random

# Create your models here.
class urlEntry(models.Model):
    size        = 4
    url_long    = models.URLField(max_length=555, unique=True,
            verbose_name="", )
    code        = models.CharField(max_length=size, unique=True)
    date        = models.DateTimeField(auto_now_add=True, auto_now=False)
    access      = models.PositiveIntegerField(default=0)
    def getcode(self, size):
        charset = string.ascii_letters + string.digits
        code = "".join([random.choice(charset) for _ in range(size)])
        if len(urlEntry.objects.filter(code = code)) > 0:
            getcode(size) # TODO hash function or short url not infinitely stored.
        return code
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.code = self.getcode(self.size)
        super(urlEntry, self).save(*args, **kwargs)
    def __unicode__(self):
        return "{0} | {1}".format(self.code, self.url_long)
    def __str__(self):
        return __unicode__(self)
    class Meta:
        verbose_name = "short Url"
        verbose_name_plural = "shor Urls"
