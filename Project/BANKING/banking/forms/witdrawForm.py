from django import forms

class WithdrawForm(forms.Form):
    amount=forms.IntegerField()
    password=forms.CharField(max_length=90,widget=forms.PasswordInput)