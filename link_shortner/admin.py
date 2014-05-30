#-*- coding: utf-8 -*-
from django.contrib import admin
from link_shortner.models import urlEntry_clear, urlEntry_ciphered

class AdminUrlEntry(admin.ModelAdmin):
    list_display    = ('code', 'access', 'url_long', 'date',)
    list_filter     = ('date',)
    date_hierarchy  = 'date'
    ordering        = ('date',)
    search_fields   = ('code', 'url_long', 'date',)

admin.site.register(urlEntry_clear, AdminUrlEntry)
admin.site.register(urlEntry_ciphered, AdminUrlEntry)
