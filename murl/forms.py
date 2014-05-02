#-*- coding: utf-8 -*-
from django import forms
from murl.models import urlEntry
from django.http import HttpRequest

class Form_newUrl(forms.ModelForm):
    class Meta:
        model = urlEntry
        fields = ('url_long',)
    def clean_url_long(self):
        url = self.cleaned_data['url_long']
        if urlEntry.objects.filter(url_long=url).exists():
            raise forms.ValidationError(
                    'Alias already exist as ' +
                    urlEntry.objects.get(url_long=url).code)
        return url
