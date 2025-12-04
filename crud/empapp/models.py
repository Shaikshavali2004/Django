from django.db import models

# Create your models here.

class Employee(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    esal = models.FloatField()
    eloc = models.CharField(max_length=32)
    
    class Meta:
        db_table = "employee"
    