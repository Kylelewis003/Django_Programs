from django.urls import path
from .views import add_project

urlpatterns = [
    path('' , add_project),
]
