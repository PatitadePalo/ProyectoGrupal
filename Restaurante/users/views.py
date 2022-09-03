from ast import USub
from multiprocessing import context
from tkinter.tix import Form
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from users.forms import User_edit_form
from django.contrib.auth.decorators import login_required

from users.models import User_profile 
from users.forms import User_registration_form 
 


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
            
                context = {"message": f"Bienvenido {username}"}
                return render(request, "start.html", context=context)

        form = AuthenticationForm()
        return render(request, "users/login.html", {"error": "Usuario o contraseña incorretos", "form":form})

    elif request.method == "GET":
        form = AuthenticationForm()
    return render(request, "users/login.html", {"form":form})

def register(request):
    if request.method == "POST":
        form = User_registration_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
        else:
            context = {"errors": form.errors}
            
            context["form"]=form
            return render(request, "users/register.html", context)

    elif request.method == "GET":  
        form = User_registration_form()
        return render(request, "users/register.html", {"form" : form})


def show_profile(request):
    if  request.user.is_authenticated:   

        return render(request, "users/profile.html")

@login_required
def update_profile(request):
    usuario = request.user.profile
    if request.method == "POST":
        myform = User_edit_form(request.POST)
        
        if myform.is_valid():                                    
            usuario.email = myform.cleaned_data["email"]
            usuario.phone = myform.cleaned_data["phone"]
            usuario.address = myform.cleaned_data["address"]                   
            usuario.save()
            
            return render(request, "users/profile.html")

    else:
        
        myform = User_edit_form(initial={
                          
            })
    
    return render(request, "users/edit_profile.html", {"myform": myform})

