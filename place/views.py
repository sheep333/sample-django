from django.db import transaction
from django.shortcuts import get_object_or_404, render

from .forms import PlaceCommentForm
from .models import Place, PlaceComment


@transaction.atomic
def detail_place(request, pk):
    place = get_object_or_404(Place, pk=pk)
    comment = PlaceComment.objects.filter(place=place)
    comment_form = PlaceCommentForm(request.POST or None)
    template = 'place/detail_place.html'

    if request.method == "POST" and comment_form.is_valid():
        new_comment = comment_form.save(commit=False)
        new_comment.place = place
        new_comment.save()
        comment_form = PlaceCommentForm()

    contexts = {
        'place': place,
        'comment': comment,
        'form': comment_form,
    }

    return render(request, template, contexts)
