from django.test import TestCase
from levenshtein.models import Levenshtein
from levenshtein.forms import LevenshteinForm


class LevenshteinTestCase(TestCase):
    def setUp(self):
        Levenshtein.objects.create(text_1="kitten", text_2="sitten")
        Levenshtein.objects.create(text_1="Translate", text_2="Transifex")

    def test_forms(self):
        """Test the form to get text_1 and text_2"""
        form_data = {'text_1': 'something', 'text_2': 'what thing'}
        form = LevenshteinForm(data=form_data)
        self.assertTrue(form.is_valid())
