#-*- coding: utf-8 -*-
from django.contrib import admin
from murl.models import urlEntry

class AdminUrlEntry(admin.ModelAdmin):
    list_display    = ('code', 'access', 'url_long', 'date',)
    list_filter     = ('date',)
    date_hierarchy  = 'date'
    ordering        = ('date',)
    search_fields   = ('code', 'url_long', 'date',)

admin.site.register(urlEntry, AdminUrlEntry)