from django.shortcuts import render
from django.http import HttpResponse

def my_blog(request):
    return HttpResponse("Hello, Blog!")  # View returns an HttpResponse as expected


# Create your views here.
