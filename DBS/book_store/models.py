from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100,unique=True)
    phone=models.BigIntegerField(unique=True)

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    title=models.CharField(max_length=50)
    rating=models.IntegerField(default=1)
    #author=models.CharField(max_length=50,default="")
    author=models.ForeignKey(Author,on_delete=models.CASCADE,null=True) # when an aouthor is delete the books are also deleted
    #author=models.ForeignKey(Author,on_delete=models.NULL) When an author is deleted the books aouthor field is null
    #author=models.ForeignKey(Author,on_delete=models.PROTECT) When an you try to delete an Error will be raised

    def __str__(self):
        return f"Book: {self.title} : Author: {self.author.name} : Rating: {self.rating}"