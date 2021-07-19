from django.shortcuts import render
from django.http import HttpResponse

#Load the home page
def index(request):
    return render(request, "home.html")

