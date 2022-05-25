from django.shortcuts import render
from django.http import HttpResponse
import random
from .data import data
from .models import Book

# Create your views here.

# All CRUD METHODS

#CREATE A Random Book
def create(request):

    no=random.randint(0,99)
    book=Book(title=data[no]['title'],author=data[no]['author'],rating=data[no]['rating'])
    book.save()

    return HttpResponse(f"Random Number Generated:{no}, The Book Saved{data[no]}")

#Get All Books:
def read_all(request):
    books=Book.objects.all()
    ul=""
    li=""
    for book in books:
        li=li+f"<h3>{book.title} , {book.author} , {book.rating}</h3>"
    ul=f"<h1>All the Books</h1><ul>{li}</ul>"
    return HttpResponse(ul)


def get_by_title(request,title):
    book=Book.objects.all().filter(title=title).first()
    
    return HttpResponse(f"<h2>The Requested Book Title: {book.title}</h2><h3>The Requsted Book Author{book.author}</h3><h4>The Requsted Book Rating{book.rating}</h4>")


## Update Book

def update_book(request,title,author):
    book=Book.objects.all().filter(title=title).first()
    book.author=author
    book.save()

    return HttpResponse(f"<h1>Book {book.title} Author {book.author} Has been updated</h1>")

## Delete Book
## book=Book.objects.all().filter(title).first()
## book.delete()

def delete(request,title):
     book=Book.objects.all().filter(title=title).first()
     book.delete()
     return HttpResponse(f"<h1>Book {book.title} Author {book.author} Has been deleted</h1>")