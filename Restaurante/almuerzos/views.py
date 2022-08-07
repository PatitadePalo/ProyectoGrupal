from django.shortcuts import render
from almuerzos.models import principal, drink, dessert
from django.http import HttpResponse
from multiprocessing import context


def food(request):
    food1 = principal.objects.create(name= "canelones" , price= 250, description= "Esta comida es muy rica", celiac= True ) 
    food2 = principal.objects.create(name= "spaghetti" , price= 200, description= "Esta comida safa", celiac= False )
    food3 = principal.objects.create(name= "bandeja paisa" , price= 500, description= "Esta comida es deliciosa", celiac= True )
    context = {
        "food1" : food1 , 
        "food2" : food2 ,
        "food3" : food3
    }
    return render(request, "food1.html", context=context)


def soda(request):
    drink1 = drink.objects.create(name= "cocacola 250 ml" , price = 150, description="esta coca es rica")
    drink2 = drink.objects.create(name= "Agua 250 ml" , price = 100, description="es muy sana")
    drink3 = drink.objects.create(name= "Fanta 250 ml" , price = 150, description="esta fanta es rica")
    context = {
        "drink1" : drink1,
        "drink2" : drink2,
        "drink3" : drink3
    }
    return render(request, "drink1.html", context=context)


def postre(request):
    dessert1= dessert.objects.create(name= "Flan" , price= 250, description= "Esta comida es muy rica", celiac= True )
    dessert2= dessert.objects.create(name= "Brownie" , price= 350, description= "Esta comida es muy rica", celiac= False)
    dessert3= dessert.objects.create(name= "Maracuya" , price= 400, description= "Esta comida es muy rica", celiac= True )
    context = {
        "dessert1" : dessert1 , 
        "dessert2" : dessert2 ,
        "dessert3" : dessert3 
    }
    return render(request, "postre1.html", context=context)


def foods_list(request):

    foods = principal.objects.all()
    context= {
        "foods": foods
    }
    return render(request, "foods_list.html", context=context)

def drinks_list(request):

    drinks = drink.objects.all()
    context= {
        "drinks": drinks
    }
    return render(request, "drinks_list.html", context=context)

def desserts_list(request):

    desserts = dessert.objects.all()
    context= {
        "desserts": desserts
    }
    return render(request, "desserts_list.html", context=context)





