from django.db import models


class Place(models.Model):
    name = models.CharField(max_length=255)
    lan = models.FloatField()
    lat = models.FloatField()
    attribute = models.CharField(max_length=50)


class PlaceComment(models.Model):
    place = models.ForeignKey(Place)
    user_name = models.CharField(max_length=50)
    text = models.TextField()