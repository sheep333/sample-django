from django.urls import path
from .views import detail_place, PlaceList

urlpatterns = [
    path('', PlaceList.as_view(), name='list_place'),
    path('detail/<int:pk>/', detail_place, name='detail_place'),
]
