from django.shortcuts import render
from .models import ProjectRegister
from django.http import HttpResponse
# Create your views here.

def add_project(request):
    if request.method == 'POST':
        form = ProjectRegister(request.POST)
        if form.is_valid(): 
            form.save()
            return HttpResponse("<h1>Record inserted successfully</h1>")
        else:
            return HttpResponse("<h1>Record not inserted</h1>")
    else:
        form = ProjectRegister()
        return render(request , "projectregister.html" , {"form" : form})