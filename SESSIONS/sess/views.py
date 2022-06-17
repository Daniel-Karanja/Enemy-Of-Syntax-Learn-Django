import re
from django.shortcuts import render
from django.http import HttpResponse
import jwt
from datetime import datetime

key="my_secret"

# Create your views here.

def create(request,key,data):
    # Assume this is the login Page:
    exp=int(datetime.now().timestamp()+15)
    jwt_token=jwt.encode({'user':{'name':'Daniel','Role':'Admin'},'exp':exp},"my_secret",algorithm="HS256")
    # request.session['k']=data
    request.session['jwt_key']=jwt_token
    return HttpResponse(f"The session Key:{key}, Session Data:{jwt_token}")

def home(request):
    token=request.session['jwt_key']
    print(token)
    user=jwt.decode(token,"my_secret",algorithms="HS256")
    print(user)
    return HttpResponse(f"The user: {user}")  

def read(request,key):
    try:
       return HttpResponse(f"The session Key:{key}, Session Data:{request.session[key]}")
    except Exception as e:
        print(e)
        return HttpResponse(f"Error Reading Session:{e}")