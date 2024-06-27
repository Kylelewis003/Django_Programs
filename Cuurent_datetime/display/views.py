from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime 
# Create your views here.

def curr_datetime(request):
    now = datetime.now()
    html =  "<html><body>Current date and time : {0} </body></html>".format(now)
    return HttpResponse(html)