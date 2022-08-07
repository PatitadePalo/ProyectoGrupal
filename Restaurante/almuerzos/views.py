from genericpath import exists
from django.shortcuts import render, redirect
from almuerzos.models import principal, drink, dessert
from django.http import HttpResponse
from multiprocessing import context
from almuerzos.forms import Formulario_principal



def food(request):
    food1 = principal.objects.create(name= "canelones" , price= 250, description= "Esta comida es muy rica", celiac= True ) 
    food2 = principal.objects.create(name= "spaghetti" , price= 200, description= "Esta comida safa", celiac= False )
    food3 = principal.objects.create(name= "bandeja paisa" , price= 500, description= "Esta comida es deliciosa", celiac= True )
    context = {
        "food1" : food1 , 
        "food2" : food2 ,
        "food3" : food3
    }
    return render(request, "foods/food1.html", context=context)


def soda(request):
    drink1 = drink.objects.create(name= "cocacola 250 ml" , price = 150, description="esta coca es rica")
    drink2 = drink.objects.create(name= "Agua 250 ml" , price = 100, description="es muy sana")
    drink3 = drink.objects.create(name= "Fanta 250 ml" , price = 150, description="esta fanta es rica")
    context = {
        "drink1" : drink1,
        "drink2" : drink2,
        "drink3" : drink3
    }
    return render(request, "drinks/drink1.html", context=context)


def postre(request):
    dessert1= dessert.objects.create(name= "Flan" , price= 250, description= "Esta comida es muy rica", celiac= True )
    dessert2= dessert.objects.create(name= "Brownie" , price= 350, description= "Esta comida es muy rica", celiac= False)
    dessert3= dessert.objects.create(name= "Maracuya" , price= 400, description= "Esta comida es muy rica", celiac= True )
    context = {
        "dessert1" : dessert1 , 
        "dessert2" : dessert2 ,
        "dessert3" : dessert3 
    }
    return render(request, "desserts/postre1.html", context=context)


def foods_list(request):

    foods = principal.objects.all()
    context= {
        "foods": foods
    }
    return render(request, "foods/foods_list.html", context=context)

def drinks_list(request):

    drinks = drink.objects.all()
    context= {
        "drinks": drinks
    }
    return render(request, "drinks/drinks_list.html", context=context)

def desserts_list(request):

    desserts = dessert.objects.all()
    context= {
        "desserts": desserts
    }
    return render(request, "desserts/desserts_list.html", context=context)

def create_food(request):
    if request.method == 'POST':
        form = Formulario_principal(request.POST)
        

        if form.is_valid():
            principal.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],
                celiac = form.cleaned_data['celiac']
            )
            
            return redirect(foods_list)

    elif request.method == 'GET':
        form = Formulario_principal()
        context = {'form':form}
        return render(request, 'foods/create_food.html', context=context)


def search_food(request):
     Restaurante = principal.objects.filter(name__icontains=request.GET['search'])
     if Restaurante.exists():
          context = {'Restaurante':Restaurante}
     else:
         Restaurante = dessert.objects.filter(name__icontains=request.GET['search'])
     if Restaurante.exists():
           context = {'Restaurante':Restaurante}
     else:   
        Restaurante = drink.objects.filter(name__icontains=request.GET['search'])
        context={"Restaurante" : Restaurante}
     search= request.GET["search"]
     return render(request, "search.html" , context=context )

