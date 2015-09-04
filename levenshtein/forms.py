from django import forms
from levenshtein.models import Levenshtein


class LevenshteinForm(forms.ModelForm):
    class Meta:
        model = Levenshtein
        exclude = (
            'distance', 'ratio', 'created_date',
        )
