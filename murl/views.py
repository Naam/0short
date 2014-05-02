from django.shortcuts import render, get_object_or_404, redirect
from murl.forms import Form_newUrl
from murl.models import urlEntry
from django.views.generic import DetailView

# Create your views here.
def create(request):
    if request.method != 'POST':
        form = Form_newUrl()
    else:
        form = Form_newUrl(request.POST)
        if form.is_valid():
            cleaned = form.save()
            url = cleaned.code
            valid = True
    return render(request, 'murl/create.html', locals())

def retrieveUrl(request, short_code):
    url = get_object_or_404(urlEntry, code=short_code)
    url.access += 1
    url.save()
    return redirect(url.url_long)
