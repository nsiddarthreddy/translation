from django.shortcuts import render

from levenshtein.models import Levenshtein
from levenshtein.forms import LevenshteinForm
from levenshtein.utils import levenshte_in_distance, levenshte_ratio


def index(request):

    levenshtein_objects = Levenshtein.objects.all()

    if request.method == 'POST':
        form = LevenshteinForm(request.POST)
        if form.is_valid():
            levenshtein = form.save()
            levenshtein.levenshtein_value = levenshte_in_distance(
                levenshtein.text_1, levenshtein.text_2)
            levenshtein.levenshtein_ratio = levenshte_ratio(
                levenshtein.text_1, levenshtein.text_2)

            levenshtein.save()
    else:
        form = LevenshteinForm()

    return render(request, 'levenshtein/index.html', {
        'form': form, 'levenshtein_objects': levenshtein_objects})
