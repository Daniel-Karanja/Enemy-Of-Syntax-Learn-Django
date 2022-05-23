from django.shortcuts import render
from .logic import to_do_list

# Create your views here.

def index(request):
    return render(request,"to_do/index.html",{"to_do_list":to_do_list})

def to_do(request,day):
    day=day.lower()
    return render(request,"to_do/to_do.html",{"day":day,"to_do":to_do_list[day]})