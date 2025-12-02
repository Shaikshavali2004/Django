from django.shortcuts import render
import datetime
# Create your views here.

def index(request):
    eid = 590
    ename = "Shaikshavali"
    return render(request, 'index.html', context={'eid': eid, 'ename': ename})

def about(request):
    mydata = {'current_time': datetime.datetime.now()}
    return render(request, 'about.html', context=mydata)

def service(request):
    return render(request, 'service.html')

def contact(request):
    return render(request, 'contact.html')