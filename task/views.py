from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect

from .models import MyTask


class MyTaskListView(LoginRequiredMixin, ListView):
    model = MyTask
    template_name = "task/task_list.html"

    def get_queryset(self):
        return MyTask.objects.filter(user=self.request.user)


@login_required
def update_mytask(request, task_id):
    if request.method == 'POST':
        mytask = get_object_or_404(MyTask, id=task_id)
        if request.user == mytask.user:
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

