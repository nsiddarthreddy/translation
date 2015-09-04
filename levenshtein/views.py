from django.views.generic import TemplateView
from levenshtein.models import Levenshtein
from levenshtein.forms import LevenshteinForm
from levenshtein.utils import levenshte_in_distance, levenshte_ratio


class LevenshteinView(TemplateView):

    template_name = 'levenshtein/index.html'

    def dispatch(self, request, *args, **kwargs):
        self.levenshtein = Levenshtein.objects.all()
        self.form = LevenshteinForm()
        return super(LevenshteinView, self).dispatch(
            request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        self.form = LevenshteinForm(request.POST)
        if self.form.is_valid():
            levenshtein = self.form.save()
            levenshtein.levenshtein_value = levenshte_in_distance(
                levenshtein.text_1, levenshtein.text_2)
            levenshtein.levenshtein_ratio = levenshte_ratio(
                levenshtein.text_1, levenshtein.text_2)
            levenshtein.save()
        return super(LevenshteinView, self).get(
            request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(LevenshteinView, self).get_context_data(**kwargs)
        context['form'] = self.form
        context['levenshtein_objects'] = self.levenshtein
        return context
