from django.urls import path
from .views import *

urlpatterns=[
    path("simple_file",simple_file,name='simple_file'),
    path("form_files",form_files,name='form_files'),
    path('model_form_file',model_form_file,name='model_form_file'),
    path('users',users,name='users'),
    ]