from .views import *
from django.urls import path

urlpatterns = [
    path("",user_login,name="user_login"),
    path("dashboard/account/<int:user_id>/<int:account_id>",my_account,name="my_account"),
    path("dashboard/handle/deposit/<int:user_id>/<int:account_id>",handle_deposit,name='handle_deposit'),
    path("dashboard/handle/withdraw/<int:user_id>/<int:account_id>",handle_withdraw,name="handle_withdraw"),
    path("dashboard/transactions/<int:account_id>",transactions,name='transactions')
]
