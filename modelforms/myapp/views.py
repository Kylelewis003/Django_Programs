from django.shortcuts import render
from .forms import mymodelform

# Create your views here.
def my_form_view(request):
    if request.method =='POST':
        form = mymodelform(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(f"Student Registered - Full name : {name} , Email : {email}")
            return render(request , 'template2.html')
    else:
        form = mymodelform()
        return render(request , 'template1.html' , {'form' : form})