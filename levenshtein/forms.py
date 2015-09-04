from django import forms

from levenshtein.models import Levenshtein

class LevenshteinForm(forms.ModelForm):
    class Meta:
        model = Levenshtein
        exclude = (
            'levenshtein_value', 'created_date',
        )
