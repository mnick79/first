from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>THe my first page</h1>")

def categories(request):
    return HttpResponse("<h1>The my second page</h1>")