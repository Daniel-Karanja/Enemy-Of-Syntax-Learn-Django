from django.urls import path
from .views import *

urlpatterns = [
    path('auth',get_mpesa_outh ),
]
