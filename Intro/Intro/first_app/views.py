from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    # print(request)
    return HttpResponse("<h1>This is the index page</h1>")

def about(request):
    return HttpResponse("<h1>This is the About page</h1>")
