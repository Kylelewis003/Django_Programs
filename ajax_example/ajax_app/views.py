from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def index(request):
    return render(request , 'ajax_app/index.html')

def ajax_submit(request):
    if request.method == 'POST' and request.is_ajax() : 
        input_data = request.POST.get('input_data')
        response_data = {'message' : 'Form submited'}
        return JsonResponse(response_data)