from django.contrib import admin

# Register your models here.
from levenshtein.models import Levenshtein

admin.site.register(Levenshtein)
