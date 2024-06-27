from django.shortcuts import render
from django.http import HttpResponse
from datetime import timedelta,datetime

# Create your views here.
def offset_datetime(request):
    now  = datetime.now()
    ahead = now + timedelta(hours=4)
    before = now - timedelta(hours=4)
    html = "<html><body>Cuurent Date and Time : {0} <br> Four hours ahead: {1} <br> Four hours before : {2}</body></html>".format(now,ahead,before)
    return HttpResponse(html)

