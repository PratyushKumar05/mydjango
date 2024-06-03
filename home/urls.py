from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index,name='home'),
    path("about", views.about,name='about'),
    path("services", views.services,name='services'),
    path("contacts", views.contacts,name='contacts'),
    path("login", views.loginUser,name='login'),
    path("dash", views.dash,name='dash'),
   
    

    

]
