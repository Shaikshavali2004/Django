from django.shortcuts import render, redirect
from empapp.forms import EmployeeForm
from empapp.models import Employee

# Create your views here.
def getcreateemp(request):
    if request.method == 'POST':
        empdata=EmployeeForm(request.POST)
        if empdata.is_valid():
            try:
                empdata.save()
                return redirect('/read')
            except:
                pass
    else:
        empform=EmployeeForm()
    return render(request, 'create.html', {'form':empform})

def getreademp(request):
    employees = Employee.objects.all()
    return render(request, 'read.html', {'employees':employees})

def getupdateemp(request,id):
    employee=Employee.objects.get(id=id)
    if request.method == 'POST':
        employee.eid = request.POST.get('eid')
        employee.ename = request.POST.get('ename')
        employee.email = request.POST.get('email')
        employee.esal = request.POST.get('esal')
        employee.eloc = request.POST.get('eloc')
        employee.save()
        return redirect('/read')
    return render(request, 'update.html', {'employee':employee})

def getdeleteemp(request,id):
    emp=Employee.objects.get(id=id)
    emp.delete()
    return redirect('/read')