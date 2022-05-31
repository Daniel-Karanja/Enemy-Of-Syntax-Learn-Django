from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.IntegerField()
    profile=models.ImageField(upload_to='profile')