from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return render(request, 'base/index.html')
    return HttpResponse('from services')

