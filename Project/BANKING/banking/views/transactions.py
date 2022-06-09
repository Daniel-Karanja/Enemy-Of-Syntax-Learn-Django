from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from banking.models import Transactions,Account,User

def transactions(request,account_id):
    acc=Account.objects.get(pk=account_id)
    trans=Transactions.objects.filter(account=acc)
    user_id=request.session['user_id']

  
    print(trans)
    return render(request,'banking/transactions.html',{ 
        'transactions':True,
        'trans':trans, 
        'account':acc    ,
        'user_id':user_id ,
        'account_id':account_id
        })