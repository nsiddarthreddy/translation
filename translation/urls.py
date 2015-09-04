from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'translation.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^levenshtein/', include('levenshtein.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
