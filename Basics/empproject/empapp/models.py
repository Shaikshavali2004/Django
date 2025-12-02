from django.db import models

# Create your models here.
class EmployeeForm(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    salary = models.IntegerField()
    location = models.CharField(max_length=64)

class UserForm(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    email = models.EmailField()