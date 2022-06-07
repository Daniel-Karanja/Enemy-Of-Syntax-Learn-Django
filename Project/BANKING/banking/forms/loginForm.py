from django import forms

class SignInForm(forms.Form):
    email=forms.EmailField(max_length=60)
    password=forms.CharField(max_length=90,widget=forms.PasswordInput)
    account_number=forms.IntegerField()

