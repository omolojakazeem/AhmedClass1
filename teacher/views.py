from django.shortcuts import render
from .models import Teacher
from sampleApp.models import Student


def teacher_home(request):
    template_name = 'teacher/index.html'
    teacher = Teacher.objects.all()
    context = {
        'page_name':'Home page for teachers',
        'my_teacher':teacher,
    }
    return render(request, template_name=template_name, context=context)


def teacher_detail(request,teacher_pk):
    template_name = 'teacher/detail.html'
    teacher = Teacher.objects.get(id=teacher_pk)
    my_students = Student.objects.filter(teacher=teacher)
    context = {
        'page_name':"Teacher's Detail",
        'teacher':teacher,
        'students':my_students
    }
    return render(request, template_name=template_name, context=context)