from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Place
from .forms import PlaceCommentFormset


class PlaceList(ListView):
    model = Place


def detail_place(request, pk):
    # FIXME: ここPOSTの時取得不要なはずなので、確認
    place = Place.objects.get(pk=pk)
    formset = PlaceCommentFormset(request.POST or None, instance=place)
    context = {'formset': formset}
    if request.method == 'POST':
        if formset.is_valid():
            formset.save()
        return redirect('post:detail_place')

    return render(request, 'post/form.html', context)
