from django import forms

from .models import Place, PlaceComment


PlaceCommentFormset = forms.inlineformset_factory(
    Place, PlaceComment, fields='__all__',
    extra=5, max_num=5, can_delete=False
)
