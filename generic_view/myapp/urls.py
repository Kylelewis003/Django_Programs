from django.urls import path
from .views import mylistview

urlpatterns = [
    path('' , mylistview.as_view() , name = 'my_list')
]
