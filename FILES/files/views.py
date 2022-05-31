from django.shortcuts import render
from .forms import *
from book_store.models import Author

# Create your views here.

def store_file(name,file):
    url=f'Global/Static/images/{name}.jpg'

    with open(url,'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

def simple_file(request):
    print(request.method)
    if request.method == 'POST':
        print(request.FILES['img'])
        store_file('mycoolpic',request.FILES['img'])
    return render(request,'files/simple_file.html')


def form_files(request):
    if request.method=='POST':
        form=AuthorForm(request.POST,request.FILES)
        
        if form.is_valid():
            
            form=AuthorForm()
            return  render(request,'files/form_files.html',{'form':form})
        return  render(request,'files/form_files.html',{'form':form})
    
    form=AuthorForm()
    return  render(request,'files/form_files.html',{'form':form})

def model_form_file(request):
    print(request.method)

    if request.method == 'POST':
        form=AuthorFormModel(request.POST,request.FILES)
        if form.is_valid():
            print('Form is Valid')
        form.save()

    form=AuthorFormModel()
    return render(request,'files/model_form_file.html',{'form':form})

def users(request):
    users=Author.objects.all()

    return render(request,'files/users.html',{'users':users})