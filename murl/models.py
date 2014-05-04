#-*- coding: utf-8 -*-
from django.db import models
from django import forms
import string
import random
from murl import crypto

# Create your models here.
class urlEntry(models.Model):
    size        = 4
    date        = models.DateTimeField(auto_now_add=True, auto_now=False)
    access      = models.PositiveIntegerField(default=0)
    code        = models.CharField(max_length=size, unique=True)
    def getcode(self, size):
        charset = string.ascii_letters + string.digits
        code = "".join([random.choice(charset) for _ in range(size)])
        if len(urlEntry_clear.objects.filter(code = code)) > 0:
            getcode(size) # TODO hash function or short url not infinitely stored.
        return code
    def save(self, *args, **kwargs):
        if self.pk is None:
            self.code = self.getcode(self.size)
        super(urlEntry, self).save(*args, **kwargs)
    def __str__(self):
        return "{0} | {1}".format(self.code, self.url_long)

class urlEntry_clear(urlEntry):
    url_long    = models.URLField(max_length=555, unique=True,
            verbose_name="", )
    ciphered    = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super(urlEntry_clear, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "short Url (plaintext)"
        verbose_name_plural = "shor Urls (plaintext)"

class urlEntry_ciphered(urlEntry):
    url_long    = models.TextField(unique=True, verbose_name="")
    key         = ""
    def save(self, *args, **kwargs):
        self.url_long, self.key = crypto.encrypt(self.url_long)
        super(urlEntry_ciphered, self).save(*args, **kwargs)
    class Meta:
        verbose_name = "short Url (ciphered)"
        verbose_name_plural = "shor Urls (ciphered)"



