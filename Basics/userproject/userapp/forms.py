from django import forms
from userapp.models import UserForm, EmpForm

class userForm(forms.Form):
    username = forms.CharField(max_length=32, label='Username')
    email = forms.EmailField(label='Email Address')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirm Password')
    

class EmpForm(forms.ModelForm):
    class Meta:
        model = EmpForm
        fields = "__all__"
    