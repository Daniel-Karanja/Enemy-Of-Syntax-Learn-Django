from django.db import models

# Create your models here.


class Owner(models.Model):
     name=models.CharField(max_length=50)
     age=models.IntegerField()
     phone=models.IntegerField()
     
class Puppy(models.Model):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    breed=models.CharField(max_length=50)
    owner=models.ForeignKey(Owner,on_delete=models.CASCADE)
    #rating= from 1 to 5
    