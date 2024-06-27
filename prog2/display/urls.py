from django.urls import path
from . import views

urlpatterns = [
    path('', views.curr_datetime, name = 'curr-datetime'),
]
