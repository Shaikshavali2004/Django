from django import forms

from empapp.models import EmployeeForm,UserForm
class EmployeeForm(forms.Form):
    name = forms.CharField(max_length=32, label='Employee Name')
    email = forms.EmailField(label='Employee Email')
    salary = forms.IntegerField(label='Employee Salary')
    location = forms.CharField(max_length=64, label='Employee Location')
    
""" class UserForm(forms.Form):
    username = forms.CharField(max_length=32, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    email = forms.EmailField(label='Email Address')  """
    
class UserForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = "__all__"
        