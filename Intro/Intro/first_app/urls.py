from django.urls import path

# from . import views
# views.index

from .views import *

urlpatterns=[
    path("",index),
    path("about",about)
]