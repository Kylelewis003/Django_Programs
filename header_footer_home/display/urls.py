from django.contrib import admin
from django.urls import path , re_path
from .views import home , aboutus , contactus

urlpatterns = [
    path('aboutus/' , aboutus),
    path('contactus/' , contactus),
    path('home/' , home),
    re_path(r'^.*$', home)
]
