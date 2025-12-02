from django.db import models

# Create your models here.
class UserForm(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField()
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    
class EmpForm(models.Model):
    emp_name = models.CharField(max_length=50)
    emp_email = models.EmailField()
    emp_department = models.CharField(max_length=50)
    emp_salary = models.DecimalField(max_digits=10, decimal_places=2)