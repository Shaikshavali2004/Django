from django.shortcuts import render
from userapp.forms import userForm, EmpForm
# Create your views here.
def gethomepage(request):
    wish = "Welcome to the User Application"
    return render(request, 'home.html', context={'wishmsg': wish})

def getuserform(request):
    userform = userForm()
    return render(request, 'user.html', {'form': userform})

def getempform(request):
    empform = EmpForm()
    return render(request, 'user.html', {'form': empform})