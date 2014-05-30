from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import Http404
from link_shortner.forms import (
        Form_newUrl_clear,
        Form_newUrl_ciph,
        Form_getUrl)
from link_shortner.models import (
        urlEntry_clear,
        urlEntry_ciphered)
from django.views.generic import DetailView
from link_shortner import crypto

# Create your views here.
def create(request):
    if request.method != 'POST':
        form = Form_newUrl_clear()
    else:
        form = Form_newUrl_clear(request.POST)
        if form.is_valid():
            if not form.cleaned_data['ciphered']:
                blob    = form.save()
            else:
                form    = Form_newUrl_ciph(request.POST)
                blob    = form.save()
                key     = blob.key
                ciphered= True
            url     = blob.code
            valid   = True
    return render(request, 'link_shortner/create.html', locals())

def get_page(short_code):
    url = urlEntry_clear.objects.filter(code=short_code)
    if not len(url) > 0:
        url = urlEntry_ciphered.objects.filter(code=short_code)
        ciphered = True
    return (url, ciphered)

def retrieveUrl(request, short_code, key=None):
    url, ciphered = get_page(short_code)
    if len(url) > 0:
        if ciphered:
            if key is not None:
                tmp = crypto.decrypt(url[0].url_long, key)
            else:
                return redirect(reverse('url_decipher',
                    kwargs={'short_code':short_code}))
        else:
            tmp = url.url_long
        url[0].access += 1
        url[0].save()
        return redirect(tmp)
    else:
        raise Http404

def getUrl(request, short_code):
    url_query = get_object_or_404(urlEntry_ciphered, code=short_code)
    if request.method != 'POST':
        # display form
        form = Form_getUrl()
        display_form = True
    else:
        form = Form_getUrl(request.POST)
        if form.is_valid():
            key = form.cleaned_data['key']
            url_clear = crypto.decrypt(url_query.url_long,
                    key)
        else:
            error = True
            error_msg = "Invalid key."
    return render(request, 'link_shortner/get_url.html', locals())

