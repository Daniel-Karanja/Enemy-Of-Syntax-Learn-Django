from django.shortcuts import render
from django.http import HttpResponse
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


# class Update_User(View):
#     def get(self,request,**kwargs):
#        print(kwargs['id'])
#     #    user=Author.objects.get(pk=kwargs['id']) # Step Get the USer.

#        form=AuthorModelForm()
#        return render(request,'forms/update.html',{'form':form})


def update_user(request,id):
    #  user=Author.objects.get(pk=id)
    #  form=AuthorModelForm(instance=user)
    #  return render(request,'forms/update.html',{'form':form})
    user=Author.objects.get(pk=id)
    print(request.method)
    if request.method == 'POST':
        form=AuthorModelForm(request.POST,instance=user)
        if form.is_valid():
            form.save()
            user=Author.objects.get(pk=id)
            return render(request,'forms/update.html',{'form':form,'id':id})

    print(user.name)
    form=AuthorModelForm(instance=user)
    return render(request,'forms/update.html',{'form':form,'id':id})
    # return HttpResponse("Update user")

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
