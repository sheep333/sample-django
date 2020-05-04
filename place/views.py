from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import Place, PlaceComment
# Create your views here.

def detail_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    comment = PlaceComment.objects.filter(place=place)
    template = ''

    contexts = {
        'place': place,
        'comment': comment,
    }
    return render(request, template, contexts)
