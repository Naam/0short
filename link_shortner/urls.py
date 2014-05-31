from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
urlpatterns = patterns('link_shortner.views',
    # Examples:
    # url(r'^$', 'mini_url.views.home', name='home'),
    url(r'^$', 'create', name='url_create'),
    url(r'^about$',
        TemplateView.as_view(template_name='link_shortner/about.html'),
        name='url_about'),
    url(r'^(?P<short_code>\w{4}).(?P<key>\w{64})$',
        'retrieveUrl', name='url_redirection_key'),
    url(r'^(?P<short_code>\w{4})', 'retrieveUrl', name='url_redirection'),
    url(r'^get/(?P<short_code>\w{4})', 'getUrl', name='url_decipher'),

)
