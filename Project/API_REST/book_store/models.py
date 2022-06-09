from django.db import models

# Create your models here.
class Puppies(models.Model):
    name = models.CharField(max_length=50)
    age = models.IntegerField()


    def __str__(self):
        return f"{self.name}"