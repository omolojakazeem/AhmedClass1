from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Student

#def index(request):
#    return HttpResponse("You are welcome to my page")


#class IndexView(View):

#    def get(self, request):
#        return HttpResponse("This is a class based view")

def home(request):
    template_name = 'student/index.html'
    student = Student.objects.all()
    context = {
        'page_name': "Home Page",
        'my_students':student,
    }
    return render(request, template_name=template_name, context=context)