from django.urls import path

from .views import MyTaskListView, update_mytask

app_name = 'task'

urlpatterns = [
    path('', MyTaskListView.as_view(), name='list'),
    path('<int:task_id>', update_mytask, name='update'),
]
