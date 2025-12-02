from django.urls import path
from webapp import views

urlpatterns = [
    path('index/', views.index),
    path('about/', views.about),
    path('service/', views.service),
    path('contact/', views.contact),
]
