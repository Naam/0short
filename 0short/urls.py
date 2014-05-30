from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mini_url.views.home', name='home'),
    url(r'^out/', include('link_shortner.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
