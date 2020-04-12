from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DeleteView, DetailView, FormView,
                                  ListView, TemplateView, UpdateView, View)

from .forms import DogForm, Sample1Form, Sample2Form, Sample3Form
from .models import Dog


# -------- GET method -------- #
def sample(request):
    """ 関数ビューサンプル """
    return HttpResponse('こんにちは！サンプルです。')


def sample1(request):
    """ テンプレートをレンダリングして表示するサンプル """
    context = {
        'text': 'こんにちは！サンプル１です。',
    }
    return render(request, 'sample/first_sample.html', context)


class Sample2(View):
    """ クラスビューサンプル """
    def get(self, request, *args, **kwargs):
        return HttpResponse('こんにちは！サンプル２です。')


# クラスをビューとして表示
class Sample3(TemplateView):
    """
    getを変更するサンプル
    基本的にはgetメソッドは上書きしないほうがいい
    """
    template_name = "sample/first_sample.html"

    # getメソッドの上書きはあまりよくない(この書き方だとエラーメッセージが出なくなる)
    # このエラーメッセージについてはurls.pyから引数を与えないようにするものなので、それさえしなければOKではある
    # 基本的には影響範囲が出なくなるようにcontextを書き換えたいときにはcontextを書き換えるのがベター
    # https://github.com/django/django/blob/master/django/views/generic/base.py#L157
    # https://github.com/django/django/blob/master/django/views/generic/base.py#L26
    def get(self, request, *args, **kwargs):
        context = {
            'text': 'こんにちは！サンプル３です。'
        }
        return self.render_to_response(context)


class Sample4(TemplateView):
    """
    get_context_dataでcontextデータを変更するサンプル
    contextを追加するだけなら元々のgetを変更しなくてもよい
    """
    template_name = 'sample/first_sample.html'

    # こちらのほうが親クラスのcontextにデータを追加するだけなので、getより影響範囲が少ない
    # 親クラスTemplateViewが既にもっているcontextデータを取得
    # 最初はcontext = {'view': self}のみを登録
    # https://github.com/django/django/blob/master/django/views/generic/base.py#L19
    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        # contextデータをdict追加
        context_data['text'] = 'こんにちは！サンプル４です。'
        return context_data


class Sample5(TemplateView):
    """ contextにいろいろな値を与えるサンプル """
    template_name = 'sample/first_sample.html'

    def get_context_data(self, **kwargs):
        # dictなのでkeyとvalueで追加できます
        context_data = super().get_context_data(**kwargs)
        context_data['num'] = 6
        context_data['text'] = [
            'こんにちは！サンプル５です。',
            '今日はいい天気ですね。',
            'こんな天気のいい日はプログラミング日和です。'
        ]
        return context_data


# -------- POST method -------- #
def post_sample(request):
    """
    ビュー関数のPOSTサンプル
    https://github.com/django/django/blob/fc0fa72ff4cdbf5861a366e31cb8bbacd44da22d/tests/test_client/views.py#L70
    """
    context = {
        'text': 'こんにちは！GETで表示します。',
    }

    if request.method == 'POST':
        context['text'] = request.POST['text']
        return render(request, 'sample/post_sample.html', context)

    return render(request, 'sample/post_sample.html', context)


# -------- POST method with Form -------- #
def post_sample1(request):
    """
    ビュー関数のPOSTサンプル
    https://github.com/django/django/blob/fc0fa72ff4cdbf5861a366e31cb8bbacd44da22d/tests/test_client/views.py#L70
    """
    # 初期値を渡すこともできます
    # Sample1Form(request.POST or None, initial={'text': '空のフォームです'})
    form = Sample1Form(request.POST or None)
    context = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        context['form'] = Sample1Form(request.POST)
        return render(request, 'sample/post_finish.html', context)

    return render(request, 'sample/form_sample1.html', context)


class Sample1Post(FormView):
    """
    フォームビューのサンプル
    https://github.com/django/django/blob/c1c68d1ac0f0d50eb37df32892b132f31a1179da/django/views/generic/edit.py#L129
    """
    form_class = Sample1Form
    template_name = 'sample/form_sample1.html'

    def form_valid(self, form):
        context = {
            'form': form
        }
        return render(self.request, 'sample/post_finish.html', context)


class Sample2Post(FormView):
    """
    フォームビューのサンプル
    フォーム丸々をまとめて表示する
    https://github.com/django/django/blob/c1c68d1ac0f0d50eb37df32892b132f31a1179da/django/views/generic/edit.py#L129
    """
    form_class = Sample2Form
    template_name = 'sample/form_sample1.html'


class Sample3Post(FormView):
    """
    フォームビューのサンプル
    それぞれのフィールドごとに表示する
    https://narito.ninja/blog/detail/98/
    """
    form_class = Sample2Form
    template_name = 'sample/form_sample2.html'


class Sample4Post(FormView):
    """
    フォームビューのサンプル
    それぞれのフィールドごとに表示する
    https://narito.ninja/blog/detail/98/
    """
    form_class = Sample3Form
    template_name = 'sample/form_sample2.html'


def create_dog(request):
    form = DogForm(request.POST or None)
    contexts = {
        'form': form,
    }

    if request.method == 'POST':
        if form.is_valid():
            # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
            form.save()
            return render(request, 'sample/post_finish.html', contexts)

    return render(request, 'sample/form_sample2.html', contexts)


class DogFormView(CreateView):
    form_class = DogForm
    template_name = 'sample/form_sample2.html'

    def form_valid(self, form):
        context = {
            'form': form
        }
        return render(self.request, 'sample/post_finish.html', context)


def list_dog(request):
    """
    https://docs.djangoproject.com/ja/3.0/topics/db/queries/
    """
    dog_list = Dog.objects.all()
    contexts = {
        'dog_list': dog_list
    }

    return render(request, 'sample/dog_list.html', contexts)


class DogListView(ListView):
    model = Dog
    template_name = "sample/dog_list.html"


def detail_dog(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    contexts = {
        'dog': dog
    }

    return render(request, 'sample/dog_detail.html', contexts)


class DogDetailView(DetailView):
    model = Dog
    template_name = "sample/dog_detail.html"


def update_dog(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    form = DogForm(request.POST or None, instance=dog)
    contexts = {
        'form': form
    }

    if request.method == 'POST' and form.is_valid():
        # save()メソッドを呼ぶだけでModelを使ってDBに登録される。
        form.save()
        return redirect('sample:list_dog')

    return render(request, 'sample/form_sample2.html', contexts)


class DogUpdateView(UpdateView):
    model = Dog
    form_class = DogForm
    success_url = '/sample/list_dog1'
    template_name = "sample/form_sample2.html"


def delete_dog(request, pk):
    dog = get_object_or_404(Dog, pk=pk)
    contexts = {
        'dog': dog,
    }

    if request.method == 'POST':
        dog.delete()
        return redirect('sample:list_dog')

    return render(request, 'sample/dog_confirm_delete.html', contexts)


class DogDeleteView(DeleteView):
    model = Dog
    success_url = reverse_lazy('sample:list_dog1')
