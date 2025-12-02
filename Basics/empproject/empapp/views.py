from django.shortcuts import render

from empapp.forms import EmployeeForm, UserForm
# Create your views here.

def gethomepage(request):
    mydata = {'msg':'Welcome to Employee Management System'}
    return render(request, 'home.html', context=mydata)


def getempForm(request):
    empform = EmployeeForm()
    return render(request, 'emp.html', {'empform': empform})

def getuserForm(request):
    userform = UserForm()
    return render(request, 'user.html', {'userform': userform})