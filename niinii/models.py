
from django.db import models

# Create your models here.


class student(models.Model):
    id=models.CharField(max_length=10,primary_key=True)
    name=models.CharField(max_length=250)
    gmail=models.CharField(max_length=250,unique=True)
    address=models.CharField(max_length=250)
    gender=models.CharField(max_length=250)
    
    
    
    
    


class Users(models.Model):
    username=models.CharField(max_length=100,primary_key=True)
    email=models.CharField(max_length=255,unique=True)
    password=models.CharField(max_length=128)
    
    