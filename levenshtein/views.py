from django.shortcuts import render
from django.views.generic import TemplateView

from levenshtein.models import Levenshtein
from levenshtein.forms import LevenshteinForm

def index(request):

    levenshtein_objects = Levenshtein.objects.all()
    
    if request.method == 'POST':
        form = LevenshteinForm(request.POST)
        if form.is_valid():
            levenshtein = form.save()
            levenshtein.levenshtein_value = levenshteinDistance(levenshtein.text_1, levenshtein.text_2)
            levenshtein.save()
    else:
        form = LevenshteinForm()

    return render(request, 'levenshtein/index.html', {'form': form, 'levenshtein_objects':levenshtein_objects})

def levenshteinDistance(s1,s2):
    if len(s1) > len(s2):
        s1,s2 = s2,s1
    distances = range(len(s1) + 1)
    for index2,char2 in enumerate(s2):
        newDistances = [index2+1]
        for index1,char1 in enumerate(s1):
            if char1 == char2:
                newDistances.append(distances[index1])
            else:
                newDistances.append(1 + min((distances[index1],
                                             distances[index1+1],
                                             newDistances[-1])))
        distances = newDistances
    return distances[-1]

