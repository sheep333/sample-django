from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect
from .models import MyTask


class MyTaskListView(ListView):
    model = MyTask
    template_name = "task/task_list.html"


def update_mytask(request, task_id):
    if request.method == 'POST':
        mytask = get_object_or_404(MyTask, id=task_id)
        mytask.finished = True
        mytask.save()
    return redirect('task:list')


'''
# 普通にアップデート画面表示するならこれでOK
class MyTaskUpdateView(UpdateView):
    model = MyTask
    fields = '__all__'
    template_name = "task/task_form.html"
    success_url = "/task"
'''

