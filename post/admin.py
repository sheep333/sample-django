from django.contrib import admin

from .models import Place, PlaceComment

# Register your models here.
admin.site.register(Place)
admin.site.register(PlaceComment)
