from django.test import TestCase
from levenshtein.forms import LevenshteinForm


class LevenshteinTestCase(TestCase):

    def test_forms(self):
        """Test the form to get text_1 and text_2"""
        form_data = {'text_1': 'something', 'text_2': 'what thing'}
        form = LevenshteinForm(data=form_data)
        self.assertTrue(form.is_valid())
