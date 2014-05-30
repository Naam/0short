#-*- coding: utf-8 -*-
from django import forms
from link_shortner.models import urlEntry_clear, urlEntry_ciphered
from django.http import HttpRequest

class Form_newUrl_clear(forms.ModelForm):
    class Meta:
        model = urlEntry_clear
        fields = ('url_long', 'ciphered')
    def clean_url_long(self):
        url = self.cleaned_data['url_long']
        if urlEntry_clear.objects.filter(url_long=url).exists():
            raise forms.ValidationError(
                    'Alias already exist as ' +
                    urlEntry_clear.objects.get(url_long=url).code)
        return url

class Form_newUrl_ciph(forms.ModelForm):
    class Meta:
        model = urlEntry_ciphered
        fields = ('url_long',)
