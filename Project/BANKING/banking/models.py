
from django.db import models
import datetime

# Create your models here.

acc_type=(
    ("Business","Business"),
    ("Personal","Personal"),
)

acc_operations=(
    ("Deposit","Deposit"),
    ("Withdraw","Withdraw"),
)

trans_status=(
    ("pending","pending"),
    ("complete","complete"),
    ("failed","failed"),
)

class User(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=60,unique=True)
    password = models.CharField(max_length=90)
    phone=models.BigIntegerField(unique=True)
    id_no=models.IntegerField()

    def __str__(self) -> str:
        return f'user:{self.name}'

class Account(models.Model):

    number=models.IntegerField(unique=True)  
    type=models.CharField(max_length=50,choices=acc_type)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    last_transaction=models.IntegerField(default=-1)
    name = models.CharField(max_length=50,blank=False)
    balance=models.BigIntegerField(default=0)

class Transactions(models.Model):
     

    type= models.CharField(default="Deposit",max_length=50,choices=acc_operations)
    amount= models.BigIntegerField(default=0)
    transaction=models.CharField(max_length=50)
    time= models.DateTimeField(default=datetime.datetime.now)
    account= models.ForeignKey(Account,on_delete=models.CASCADE)
    status=models.CharField(max_length=50,blank=True,choices=trans_status)
