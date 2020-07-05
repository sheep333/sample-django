from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Place(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    lan = models.DecimalField(decimal_places=10, max_digits=10)
    lat = models.DecimalField(decimal_places=10, max_digits=10)
    created_time = models.DateTimeField(auto_now=True)
    updated_time = models.DateTimeField(auto_now_add=True)


class PlaceComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    place = models.ForeignKey(Place, on_delete=models.CASCADE)
    content = models.TextField()
