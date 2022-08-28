from tkinter.tix import CheckList
from django import forms

class Formulario_principal(forms.Form):
    name = forms.CharField(max_length=40, label= "Nombre")
    price = forms.FloatField(label="Precio")
    description = forms.CharField(max_length=200, label= "Descripción")
    celiac = forms.BooleanField(required=False, label="Apto celiaco")
    image = forms.ImageField(required=False)

class Formulario_drink(forms.Form):
    name = forms.CharField(max_length=40, label= "Nombre")
    price = forms.FloatField(label="Precio")
    description = forms.CharField(max_length=200, label= "Descripción",required=False)

class Formulario_dessert(forms.Form):
    name = forms.CharField(max_length=40, label= "Nombre")
    price = forms.FloatField(label="Precio")
    description = forms.CharField(max_length=200, label= "Descripción")
    celiac = forms.BooleanField(required=False, label="Apto celiaco")