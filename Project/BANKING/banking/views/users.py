from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse


from banking.forms.loginForm import SignInForm
from banking.forms.depositForm import DepositForm
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


    user= User.objects.get(pk=user_id)
    
    acc=Account.objects.get(pk=account_id)

    deposit_form=DepositForm()

    return render(request,'banking/my_account.html',{
                           'myAccount':True,
                           'account':acc,
                           'user':user,
                           'deposit_form':deposit_form,
                           'show_panel':True, 
                           'panel_color':'w3-green',
                           'panel_message':f'Welcome {user.name}',
                           'panel_message_class':'w3-center thick-text'
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
            # Mpesa Deposit
            # Make Request to the mpesa server for stk push.
            # Best Case Deposit goes through
            # We will handle failed transactions later
            account.balance=account.balance+amount    
            account.save()   
            return HttpResponseRedirect(reverse('my_account',kwargs={'user_id': user.id,'account_id':account.id}))

    return HttpResponse("Handling the deposit")