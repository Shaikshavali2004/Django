from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=32)
    esal = models.FloatField()
    eloc = models.CharField(max_length=32)
    
class User(models.Model):
    uname = models.CharField(max_length=32)
    uemail = models.EmailField()
    upassword = models.IntegerField()
    uloc = models.CharField(max_length=32)