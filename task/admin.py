from django.contrib import admin

from .models import Category, MyTask, Task

admin.site.register(Task)
admin.site.register(Category)
admin.site.register(MyTask)
