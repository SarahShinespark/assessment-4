from django.shortcuts import render
from django.http import HttpResponse

#Controllers for the "categories" pages

def index(request):
    return HttpResponse("Hello, world. You're at the categories index.")