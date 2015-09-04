from django.shortcuts import render

from levenshtein.models import Levenshtein
from levenshtein.forms import LevenshteinForm


def index(request):

    levenshtein_objects = Levenshtein.objects.all()

    if request.method == 'POST':
        form = LevenshteinForm(request.POST)
        if form.is_valid():
            levenshtein = form.save()
            levenshtein.levenshtein_value = levenshte_in_distance(
                levenshtein.text_1, levenshtein.text_2)

            levenshtein.save()
    else:
        form = LevenshteinForm()

    return render(request, 'levenshtein/index.html', {
        'form': form, 'levenshtein_objects': levenshtein_objects})


def levenshte_in_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1
    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1],
                                             distances[index1 + 1],
                                             new_distances[-1])))
        distances = new_distances
    return distances[-1]
