from django.shortcuts import render
from django.http import HttpResponse

# from .tasks import writeFiles

def home(request):
    url = request.GET.get('url', "http://test.com.bd")
    # writeFiles.delay(url)
    return HttpResponse("home page")
