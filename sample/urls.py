from django.urls import path
from .views import (
    sample, sample1, Sample2, Sample3, Sample4, Sample5, post_sample, post_sample1,
    Sample1Post, Sample2Post, Sample3Post, Sample4Post, create_dog, DogFormView,
    DogListView, list_dog, detail_dog, DogDetailView, update_dog, DogUpdateView,
    delete_dog, DogDeleteView
)
from django.views.generic import TemplateView

app_name = 'sample'

urlpatterns = [
    path('sample/', sample, name='sample'),
    path('sample1/', sample1, name='sample1'),
    path('sample2/', Sample2.as_view(), name='sample2'),
    path('sample3/', Sample3.as_view(), name='sample3'),
    path('sample4/', Sample4.as_view(), name='sample4'),
    path('sample5/', Sample5.as_view(), name='sample5'),
    path('post_sample/', post_sample, name='post_sample'),
    path('post_sample_1/', post_sample1, name='post_sample_1'),
    path('post_sample1/', Sample1Post.as_view(), name='post_sample1'),
    path('post_sample2/', Sample2Post.as_view(), name='post_sample2'),
    path('post_sample3/', Sample3Post.as_view(), name='post_sample3'),
    path('post_sample4/', Sample4Post.as_view(), name='post_sample4'),
    path('post_finish/', TemplateView.as_view(template_name='sample/post_finish.html'), name='post_finish'),
    path('create_dog/', create_dog, name='create_dog'),
    path('create_dog1/', DogFormView.as_view(), name='create_dog1'),
    path('list_dog/', list_dog, name='list_dog'),
    path('list_dog1/', DogListView.as_view(), name='list_dog1'),
    path('detail_dog/<int:pk>/', detail_dog, name='detail_dog'),
    path('detail_dog1/<int:pk>/', DogDetailView.as_view(), name='detail_dog1'),
    path('update_dog/<int:pk>/', update_dog, name='update_dog'),
    path('update_dog1/<int:pk>/', DogUpdateView.as_view(), name='update_dog1'),
    path('delete_dog/<int:pk>/', delete_dog, name='delete_dog'),
    path('delete_dog1/<int:pk>/', DogDeleteView.as_view(), name='delete_dog1')
]
