from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import time
import urllib3
import json

http = urllib3.PoolManager()


from banking.forms.loginForm import SignInForm
from banking.forms.depositForm import DepositForm
from banking.forms.witdrawForm import WithdrawForm
from banking.models import *

def user_login(request):

    if request.method == 'POST':
        form=SignInForm(request.POST)

        if form.is_valid():
           
           try:
                email=form.cleaned_data['email']
                password=form.cleaned_data['password']
                account=form.cleaned_data['account_number']
                user=User.objects.filter(email=email,password=password)[0]
                account=Account.objects.filter(number=account)[0]
                return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))
           except Exception as e:   
                     form = SignInForm()
                     return render(request,'banking/login.html',
                            {'page_title':'Sign In','show_panel':True,
                            'panel_color':'w3-red','panel_message':
                            '!!! Hey User Or Account Not Found Try Again','panel_message_class':'w3-center thick-text',
                            'form':form})
           
        return render(request,'banking/login.html',
                    {'page_title':'Sign In','show_panel':True,
                    'panel_color':'w3-red','panel_message':
                    '!! Form Error','panel_message_class':'w3-center thick-text',
                    'form':form})
    form = SignInForm()

    return render(request,'banking/login.html',
    {'page_title':'Sign In','show_panel':False,
    'panel_color':'w3-blue','panel_message':
    'My first panel message','panel_message_class':'w3-center thick-text',
    'form':form})


def my_account(request,user_id,account_id):
    print(user_id)
    print(account_id)
    
    show_panel=False
    panel_color=''
    panel_message=''
    panel_message_class='w3-center thick-text'

    last_trans='None'
    request.session['user_id']=user_id

    user= User.objects.get(pk=user_id)
    
    acc=Account.objects.get(pk=account_id)

    deposit_form=DepositForm()
    withdraw_form=WithdrawForm()

    if acc.last_transaction != -1:
       trans=Transactions.objects.get(pk=acc.last_transaction)
       last_trans=f'{trans.type}, Amount: {trans.amount} Ksh'
      


    if 'cust_mess' in request.session :
        if request.session['cust_mess'] ==True:
            request.session['cust_mess']=False
            show_panel=request.session['show_panel']
            panel_message=request.session['panel_message']
            panel_color=request.session['panel_color']

    return render(request,'banking/my_account.html',{
                           'myAccount':True,
                           'user_id':user_id,
                           'account_id':account_id,
                           'account':acc,
                           'user':user,
                           'deposit_form':deposit_form,
                           'withdraw_form':withdraw_form,
                           'last_trans':last_trans,
                           'show_panel':show_panel, 
                           'panel_color':panel_color,
                           'panel_message':panel_message,
                           'panel_message_class':panel_message_class
                           })

def handle_deposit(request,user_id,account_id):

    user= User.objects.get(pk=user_id)
    
    account=Account.objects.get(pk=account_id)

    if request.method == 'POST':
        deposit_form=DepositForm(request.POST)
        print(deposit_form.is_valid())
        if deposit_form.is_valid():
            amount=deposit_form.cleaned_data['amount']
            phone=deposit_form.cleaned_data['phone']

            if amount <0:
                print("!!! Hey You Cant Deposit A Negative Amount")
                request.session['cust_mess']=True 
                request.session['show_panel']=True
                request.session['panel_message']='You cant deposit a negative amount'
                request.session['panel_color']='w3-red'
                return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))
           
            # Mpesa Deposit
            # Make Request to the mpesa server for stk push.
            # Best Case Deposit goes through
            # We will handle failed transactions later
            url="http://127.0.0.1:7000/mpesa/stk/push"
            payload=json.dumps({
                "phone":phone,
                "amount":amount
            }).encode("utf8")
            res=http.request(method='POST', url=url,body=payload,headers={
                'Content-Type': 'application/json'
            })
            data=json.loads(res.data.decode('utf-8'))
            print(data)
            trans=Transactions(amount=amount,transaction=data[payload]['CheckoutRequestID'],account=account,status="pending")
            trans.save()

            # account.balance=account.balance+amount   
            account.last_transaction=trans.id 
            account.save()   
            request.session['cust_mess']=True 
            request.session['show_panel']=True
            request.session['panel_message']=f'Success {data["payload"]["ResponseDescription"]}.Go To transactions page to verify the transaction'
            request.session['panel_color']='w3-green'
            return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))
        request.session['cust_mess']=True 
        request.session['show_panel']=True
        request.session['panel_message']='!!Check Form,its invalid'
        request.session['panel_color']='w3-red'
        return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))

    request.session['cust_mess']=True 
    request.session['show_panel']=True
    request.session['panel_message']='!!!! Error Processing transaction. Contact Admin'
    request.session['panel_color']='w3-red'
    return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))



def handle_withdraw(request,user_id,account_id):
    
    
    request.session['show_panel']=True
    request.session['panel_color']='w3-red'

    user= User.objects.get(pk=user_id)
    
    account=Account.objects.get(pk=account_id)

    if request.method == 'POST':
        deposit_form=WithdrawForm(request.POST)
        if deposit_form.is_valid():
            amount=deposit_form.cleaned_data['amount']
            password=deposit_form.cleaned_data['password']
            
            if user.password != password:
                print("Throw an Error")
                request.session['cust_mess']=True 
                request.session['panel_message']='!!! Enter Corect Password To Withdraw'
                return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))

            # Mpesa Deposit
            # Make Request to the mpesa server for stk push.
            # Best Case Deposit goes through
            # We will handle failed transactions later
            # account.balance=account.balance+amount    
            # account.save()   
            # trans=Transactions(amount=amount,transaction=time.time(),account=account)
            # trans.save()

            if account.balance < amount:
                print("You dont have enough cash")
                request.session['cust_mess']=True       
                request.session['panel_message']=f'You Dont have enough cash in your account <br>Your Acount Balance is {account.balance } <br>Amount To Withdraw:{amount}<br>Work within your means !!!!!!!!!!!!!!!!'
                return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))
           
            
              
            trans=Transactions(type="Withdraw",amount=amount,transaction=time.time(),account=account)
            trans.save()
            account.balance=account.balance-amount  
            account.last_transaction=trans.id 
            account.save() 
            request.session['panel_color']='w3-green'
            request.session['panel_message']=f'Success, {amount} has been withdrawn'
            return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))
    
    request.session['panel_message']='!!!! Error Processing Withdraw transaction. Contact Admin'
    request.session['panel_color']='w3-red'
    return HttpResponse("Handling the Withdraw")