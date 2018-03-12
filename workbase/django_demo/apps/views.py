from django.shortcuts import render, HttpResponse

# Create your views here.


def hello(req):
    return HttpResponse('Hello World')