from django import forms

class DepositForm(forms.Form):
    phone =forms.IntegerField()
    amount=forms.IntegerField()
