from django.shortcuts import render
from empapp.forms import EmployeeForm, UserForm
from empapp.models import Employee, User
# Create your views here.
def gethomepage(request):
    return render(request, 'home.html', {'wish':"Welcome to Home Page"})

def getregister(request):
    empform=EmployeeForm()
    return render(request, 'emp.html', {'form':empform})

def saveemp(request):
    if request.method == 'POST':
        empdata=EmployeeForm(request.POST)
        if(empdata.is_valid()):
            empdata.save()
    return render(request, 'save.html')

def newuser(request):
    userform = UserForm()
    return render(request, 'user.html', {'form':userform})
    
def saveuser(request):
    if request.method == 'POST':
        uname = request.POST.get('uname')
        uemail = request.POST['uemail']
        upassword = request.POST['upassword']
        uloc = request.POST['uloc']
        userdata=User(uname=uname,uemail=uemail,upassword=upassword,uloc=uloc)
        userdata.save()
    return render(request, 'success.html')