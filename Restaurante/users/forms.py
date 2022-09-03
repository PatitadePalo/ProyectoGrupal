import email
from logging import PlaceHolder
from socket import fromshare
from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.contrib.auth.models import User
from django import forms

class User_registration_form(UserCreationForm):
    email = forms.EmailField(required= True)
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

        help_texts = { k : "" for k in fields}

class User_edit_form(forms.ModelForm):
    email =forms.EmailField(label = "Modificar E-mail")
    phone = forms.CharField(max_length=20, label = "Modificar Teléfono")
    address = forms.CharField(max_length=200, label = "Modificar dirección")
    
    class Meta:
        model = User
        fields = ("email", "phone", "address")
        help_texts = { k : "" for k in fields}

    
