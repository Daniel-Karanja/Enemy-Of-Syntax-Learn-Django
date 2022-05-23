from django.urls import path
from .views import *

urlpatterns = [
  path("",index,name="to_do"),
  path("<day>",to_do,name="to_do_day")
]