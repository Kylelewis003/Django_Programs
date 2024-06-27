from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def aboutus(request):
    return render(request , 'aboutus.html')

def contactus(request):
    return render(request , 'contactus.html')

def home(request):
    return render(request , 'home.html')
