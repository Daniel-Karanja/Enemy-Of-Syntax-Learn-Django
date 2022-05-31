from django import forms
from bookstore.models import Author


class AuthorModelForm(forms.ModelForm):
    class Meta:
        model=Author
        fields=['name','email','phone']
        #fields="__all__"  This will get all the fields
        #exclude=['email'] This will excklude the firelds
 
         