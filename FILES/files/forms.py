from django import forms
from book_store.models import Author

class AuthorForm(forms.Form):
    image=forms.FileField()
    name=forms.CharField(max_length=50)

class AuthorFormModel(forms.ModelForm):
    class Meta:
        model = Author
        fields ="__all__"

        labels={
            'name':"Enter Author Name",
            'email':'Enter Author Email',
            'phone':'Enter Author Phone Number',
            'profile':'Upload Profile Picture'
        }