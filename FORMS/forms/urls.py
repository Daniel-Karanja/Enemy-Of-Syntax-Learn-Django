from django.urls import path 
from .views import *

urlpatterns =[
    path("model_form",model_form,name='model_form'),
    path('class/model_form',Model_Form.as_view(),name='class_model_form'),
    path('update/<int:id>',Update_User.as_view(),name='update_user')
    ]