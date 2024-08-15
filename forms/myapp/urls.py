from django.urls import path
from . import views

urlpatterns = [
    path('' , views.my_for_view , name='forms')
]
