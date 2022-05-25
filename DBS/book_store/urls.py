from django.urls import path
from .views import *

urlpatterns = [
    path('create/',create ),
    path("read/",read_all),
    path("read/<title>/",get_by_title),
    path("update/<title>/<author>",update_book),
    path("delete/<title>",delete)
]
