from django.shortcuts import render, get_object_or_404, redirect
from murl.forms import Form_newUrl_clear, Form_newUrl_ciph
from murl.models import urlEntry_clear, urlEntry_ciphered
from django.views.generic import DetailView
from murl import crypto

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
    return render(request, 'murl/create.html', locals())

def retrieveUrl_clear(request, short_code):
    return retrieveUrl_ciphered(request, short_code, None)

def retrieveUrl_ciphered(request, short_code, key):
    if not key is None:
        url = get_object_or_404(urlEntry_ciphered, code=short_code)
        tmp = crypto.decrypt(url.url_long, key)
    else:
        url = get_object_or_404(urlEntry_clear, code=short_code)
        tmp = url.url_long
    url.access += 1
    url.save()
    return redirect(tmp)
