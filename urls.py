from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()
from django.views.generic import RedirectView

urlpatterns = patterns('',
    url(r'^admin42/', include(admin.site.urls)),
    url(r'^api42/', include('while42.urls')),
    # url(r'^', RedirectView.as_view(url='http://while42.org/')),
)