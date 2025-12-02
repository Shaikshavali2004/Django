from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Welcome to Home Page!")

def about(request):
    return HttpResponse("This is the About Page.")

def services(request):
    return HttpResponse("Our Services are listed here.")

def contact(request):
    return HttpResponse("Contact us at +91 1234567890 +91 9876543210")