from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome to the Home Page of User App")

def about(request):
    return HttpResponse("This is the About Page of User App")

def services(request):
    return HttpResponse("This is the Services Page of User App")

def contact(request):
    return HttpResponse("This is the Contact Page of User App")
