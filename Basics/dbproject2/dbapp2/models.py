from django.db import models


# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=24)
    price = models.IntegerField()
    qty = models.IntegerField()
    mfg = models.DateField()
    
    
""" class Order(models.Model):
    orderno = models.CharField(max_length=12)
    orderdate = models.DateField()
    location = models.CharField(max_length=32) """