#-*- coding: utf-8 -*-
from django import forms
from link_shortner.models import urlEntry_clear, urlEntry_ciphered
from django.http import HttpRequest

class Form_newUrl_clear(forms.ModelForm):
    ciphered = forms.NullBooleanField(initial=False, widget=forms.CheckboxInput)
    class Meta:
        model = urlEntry_clear
        fields = ('url_long',)

class Form_newUrl_ciph(forms.ModelForm):
    class Meta:
        model = urlEntry_ciphered
        fields = ('url_long',)

class Form_getUrl(forms.Form):
    key = forms.CharField(min_length=64, max_length=64)
