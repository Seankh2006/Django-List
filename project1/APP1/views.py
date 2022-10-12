from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def file1(request):
    return HttpResponse("Welcome")

def file3(request, name):
    return HttpResponse(f"Hello, {name}!")
