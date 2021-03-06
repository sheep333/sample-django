from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Task(models.Model):
    category = models.ForeignKey("Category", on_delete=models.CASCADE)
    content = models.CharField(max_length=255)

    def __str__(self):
        return self.content


class MyTask(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
