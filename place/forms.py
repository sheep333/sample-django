from django import forms

from .models import Place

# inline_formsetでPlaceとPlaceCommentを同時に取得
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'


class PlaceCommentForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'