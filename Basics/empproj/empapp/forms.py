from django import forms
from empapp.models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['eid','ename','esal','eloc']
        
        
class UserForm(forms.Form):
    uname = forms.CharField(max_length=32, label='User Name')
    uemail = forms.EmailField(label='User Email')
    upassword = forms.IntegerField(label='User Password')
    uloc = forms.CharField(max_length=32,label='User Location')