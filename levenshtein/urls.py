from django.conf.urls import url
from levenshtein import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
