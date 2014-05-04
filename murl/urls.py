from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
urlpatterns = patterns('murl.views',
    # Examples:
    # url(r'^$', 'mini_url.views.home', name='home'),
    url(r'^$', 'create', name='url_create'),
    url(r'^(?P<short_code>\w{4}).(?P<key>\w{64})$',
        'retrieveUrl_ciphered', name='url_redirection_ciphered'),
    url(r'^(?P<short_code>\w{4})$',
        'retrieveUrl_clear', name='url_redirection_clear'),
    url(r'^about$', TemplateView.as_view(template_name='murl/.html')),
)
