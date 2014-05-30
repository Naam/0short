from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from link_shortner.forms import Form_newUrl_clear, Form_newUrl_ciph
from link_shortner.models import urlEntry_clear, urlEntry_ciphered
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

#def retrieveUrl_clear(request, short_code):
#    return retrieveUrl_ciphered(request, short_code, None)

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
                raise Http404 # FIXME view enter key
        else:
            tmp = url.url_long
        url[0].access += 1
        url[0].save()
        return redirect(tmp)
    else:
        raise Http404
