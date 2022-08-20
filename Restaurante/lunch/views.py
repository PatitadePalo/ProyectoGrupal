from genericpath import exists
from django.shortcuts import render, redirect
from lunch.models import principal, drink, dessert
from django.http import HttpResponse
from multiprocessing import context
from lunch.forms import Formulario_principal, Formulario_drink, Formulario_dessert
from itertools import chain


def food(request):
    food1 = principal.objects.create(name= "canelones" , price= 255, description= "Relleno de espinaca y ricota, envuelto en un.", celiac= True ) 
    context = {
        "food1" : food1 ,        
    }
    return render(request, "foods/food1.html", context=context)


def soda(request):
    drink1 = drink.objects.create(name= "cocacola 250 ml" , price = 150, description="esta coca es rica")

    context = {
        "drink1" : drink1,
    }
    return render(request, "drinks/drink1.html", context=context)


def sweet_dish(request):
    dessert1= dessert.objects.create(name= "Flan" , price= 250, description= "Esta comida es muy rica", celiac= True )
    context = {
        "dessert1" : dessert1 ,        
    }
    return render(request, "desserts/sweet dish.html", context=context)


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
    principal_search= principal.objects.filter(name__icontains=request.GET['search'])
    drink_search= drink.objects.filter(name__icontains=request.GET['search'])
    dessert_search  = dessert.objects.filter(name__icontains=request.GET['search'])

    result_list = list(chain(principal_search, drink_search, dessert_search))    
    
    context = {'result_list':result_list}
       
    search= request.GET["search"]
    return render(request, "search.html" , context=context, )

def start(request):
    return render(request, "start.html",context={})

def add_food(request):
    return render(request, "add_food.html",context={})

def create_drink(request):
    if request.method == 'POST':
        form = Formulario_drink(request.POST)
        

        if form.is_valid():
            drink.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],                
            )
            
            return redirect(drinks_list)

    elif request.method == 'GET':
        form = Formulario_drink()
        context = {'form':form}
        return render(request, 'drinks/create_drink.html', context=context)


def create_dessert(request):
    if request.method == 'POST':
        form = Formulario_dessert(request.POST)
        

        if form.is_valid():
            dessert.objects.create(
                name = form.cleaned_data['name'],
                price = form.cleaned_data['price'],
                description = form.cleaned_data['description'],                
                celiac = form.cleaned_data['celiac']
            )
            
            return redirect(desserts_list)

    elif request.method == 'GET':
        form = Formulario_dessert()
        context = {'form':form}
        return render(request, 'desserts/create_dessert.html', context=context)


# def search_food2(request):
#     principal_search= principal.objects.filter(name__icontains=request.GET['search'])
#     drink_search= drink.objects.filter(name__icontains=request.GET['search'])
#     dessert_search  = dessert.objects.filter(name__icontains=request.GET['search'])

#     result_list = list(chain(principal_search, drink_search, dessert_search))    
    
#     if context = {'result_list':result_list}
       
#     search= request.GET["search"]
#     return render(request, "search.html" , context=context, )

#     else: 
#     return render(request "search.html, no se encuentra este producto