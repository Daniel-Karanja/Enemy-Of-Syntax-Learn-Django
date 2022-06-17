from django.urls import path
from .views import *

urlpatterns = [
    path('auth',get_mpesa_outh ),
    path('stk/push',stkPush),
    path('stk/query',stkQuery),
    path("time",mpesa_time_stamp)
]
