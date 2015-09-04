from django.conf.urls import url
from levenshtein.views import LevenshteinView

urlpatterns = [
    url(r'^$', LevenshteinView.as_view(), name='index'),
]
