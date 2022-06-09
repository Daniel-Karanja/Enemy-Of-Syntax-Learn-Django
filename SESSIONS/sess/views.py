from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def create(request,key,data):
    request.session[key]=data
    return HttpResponse(f"The session Key:{key}, Session Data:{data}")

def read(request,key):
    try:
       return HttpResponse(f"The session Key:{key}, Session Data:{request.session[key]}")
    except Exception as e:
        print(e)
        return HttpResponse(f"Error Reading Session:{e}")