from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
import time



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

    


    user= User.objects.get(pk=user_id)
    
    acc=Account.objects.get(pk=account_id)

    deposit_form=DepositForm()

    if 'cust_mess' in request.session :
        if request.session['cust_mess'] ==True:
            request.session['cust_mess']=False
            show_panel=request.session['show_panel']
            panel_message=request.session['panel_message']
            panel_color=request.session['panel_color']

    return render(request,'banking/my_account.html',{
                           'myAccount':True,
                           'account':acc,
                           'user':user,
                           'deposit_form':deposit_form,
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
            account.balance=account.balance+amount    
            account.save()   
            trans=Transactions(amount=amount,transaction=time.time(),account=account)
            trans.save()
            return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))

    return HttpResponse("Handling the deposit")


def handle_withdraw(request,user_id,account_id):

    user= User.objects.get(pk=user_id)
    
    account=Account.objects.get(pk=account_id)

    if request.method == 'POST':
        deposit_form=WithdrawForm(request.POST)
        if deposit_form.is_valid():
            amount=deposit_form.cleaned_data['amount']
            password=deposit_form.cleaned_data['password']
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
                request.session['show_panel']=True
                request.session['panel_message']=f'You Dont have enough cash in your account <br>Your Acount Balance is {account.balance } <br>Amount To Withdraw:{amount}<br>Work within your means !!!!!!!!!!!!!!!!'
                request.session['panel_color']='w3-red'
                return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))
           
            
            account.balance=account.balance-amount   
            account.save()   
            trans=Transactions(type="Withdraw",amount=amount,transaction=time.time(),account=account)
            trans.save()
            return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))

    return HttpResponse("Handling the Withdraw")