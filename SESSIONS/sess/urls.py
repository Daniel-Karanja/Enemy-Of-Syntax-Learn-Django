from django.urls import path
from .views import *

urlpatterns = [
   path('create/<key>/<data>',create),
   path('read/<key>',read),
   path("home",home)
]
