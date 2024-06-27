from django.shortcuts import render

# Create your views here.
def list_view(request):
    fruits = ['apple' , 'banana' , 'cherry']
    students = ['alice' , 'bob' , 'charlie']
    
    context = {
        'fruits' : fruits,
        'students' : students
    }
    
    return render (request , 'list_view.html' , context)