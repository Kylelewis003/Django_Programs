from django.shortcuts import render
from .forms import Myform
# Create your views here.

def my_for_view(request):
    if request.method == 'POST':
        form = Myform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(f"Student Registered - Full name : {name} , Email : {email}")
            return render(request , 'template2.html')
    else:
        form = Myform()
        return render(request , 'template1.html' , {'form' : form})
                