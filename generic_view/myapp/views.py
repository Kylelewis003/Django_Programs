from django.shortcuts import render
from django.views.generic import ListView
from .models import Book

# Create your views here.
class mylistview(ListView):
    model = Book
    template_name = r'C:\django\generic_view\myapp\templates\my_model_template.html'
    context_object_name = 'books'
