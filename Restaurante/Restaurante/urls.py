"""Restaurante URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from almuerzos.views import food, soda, foods_list, drinks_list, desserts_list, postre, create_food, search_food, inicio, agregar_comida,create_drink, create_dessert
urlpatterns = [
    path('admin/', admin.site.urls),
    path("food1/", food , name="food1"),
    path("drink1/", soda , name = "drink1"),
    path("foods_list/", foods_list , name="foods_list"),
    path("drinks_list/", drinks_list , name="drinks_list"),
    path("postre1/", postre, name="postre1" ),
    path("desserts_list/", desserts_list, name="desserts_list"),
    path("create_food/", create_food , name="create_food" ),
    path("create_drink/", create_drink, name="create_drink"),
    path("create_dessert/", create_dessert, name="create_dessert"),
    path("search_food/" , search_food , name ="search_food"),
    path("inicio/", inicio, name= "inicio"),
    path("agregar_comida/", agregar_comida , name="agregar_comida")
]
