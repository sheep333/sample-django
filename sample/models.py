from django.db import models


class Dog(models.Model):
    """
    Djangoのモデルフィールド
    https://docs.djangoproject.com/ja/3.0/ref/models/fields/
    """
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    kind = models.CharField(max_length=255)
    birthday = models.DateField()
