from django.urls import path
from ajax_app import views
urlpatterns = [
    path('' , views.index , name = 'index'),
    path('ajax/submit/' , views.ajax_submit , name = 'ajax_submt')
]
