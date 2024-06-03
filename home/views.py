from django.shortcuts import render,HttpResponse,redirect
from home.models import Contacts
from django.contrib.auth.models import User
from django.contrib.auth import logout,authenticate,login
# Create your views here.
def index (request):
    return render(request, 'index.html')

def about (request):
     return render(request, 'about.html')
   

def services (request):
     return render(request, 'services.html')

def contacts (request):
    if request.method=="POST":
        name = request.POST.get('name')

        email = request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contacts=Contacts(name=name, email=email,phone=phone, desc=desc)
        contacts.save
    return render(request, 'contact.html')

def loginUser(request):
    return render(request, 'login.html')

def dash(request):
    return render(request, 'dash.html')
 