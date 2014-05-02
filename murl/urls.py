from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
urlpatterns = patterns('murl.views',
    # Examples:
    # url(r'^$', 'mini_url.views.home', name='home'),
    url(r'^$', 'create', name='url_create'),
    url(r'^(?P<short_code>\w{4})$', 'retrieveUrl', name='url_redirection'),
    url(r'^non$', TemplateView.as_view(template_name='murl/non.html')),
)
