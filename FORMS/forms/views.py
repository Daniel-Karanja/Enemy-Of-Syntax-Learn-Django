from django.shortcuts import render
from .forms import AuthorModelForm
from django.views import View
from bookstore.models import Author

# Create your views here.

class Model_Form(View):
    def get(self,request):
        form=AuthorModelForm()
        return render(request,'forms/class_model_form.html',{'form':form})
    
    def post(self,request):
        form = AuthorModelForm(request.POST)
        if form.is_valid():
            form.save()
            form=AuthorModelForm()
            return render(request,'forms/class_model_form.html',{'form':form})
        return render(request,'forms/class_model_form.html',{'form':form})


class Update_User(View):
    def get(self,request,*args,**kwargs):
       user=Author.objects.get(pk=kwargs['id']) # Step Get the USer.
       form=AuthorModelForm(instance=user)
       return render(request,'forms/update.html',{'form':form})
    

def model_form(request):
    print(request.method)
    if request.method == 'POST':
        form = AuthorModelForm(request.POST)
        if form.is_valid():
            form.save()
            form=AuthorModelForm()
            return render(request,'forms/model_form.html',{'form':form})
        return render(request,'forms/model_form.html',{'form':form})
    form=AuthorModelForm()
    return render(request,'forms/model_form.html',{'form':form})
