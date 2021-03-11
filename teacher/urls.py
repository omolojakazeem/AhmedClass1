from django.urls import path
from .views import teacher_home,teacher_detail

urlpatterns = [
    path('',teacher_home, name='teacher_homepage'),
    path('detail/<int:teacher_pk>',teacher_detail, name='teacher_detail'),
]