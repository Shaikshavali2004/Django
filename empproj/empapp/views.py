from django.shortcuts import render
from empapp.forms import EmployeeForm
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