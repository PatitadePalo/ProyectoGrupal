from tkinter.tix import CheckList
from django import forms

class Formulario_principal(forms.Form):
    name = forms.CharField(max_length=40)
    price = forms.FloatField()
    description = forms.CharField(max_length=200)
    celiac = forms.BooleanField(required=False, label="Apto celiaco")