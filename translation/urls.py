from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^levenshtein/', include('levenshtein.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
