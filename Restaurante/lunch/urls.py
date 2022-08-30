from django.urls import path

from lunch.views import food, soda, foods_list, drinks_list, sweet_dish, desserts_list, create_food, create_drink, \
create_dessert, add_food, update_food, update_drink, update_dessert, Delete_food, Delete_dessert, Delete_drink


urlpatterns = [
    path("food1/", food , name="food1"),
    path("drink1/", soda , name = "drink1"),
    path("foods_list/", foods_list , name="foods_list"),
    path("drinks_list/", drinks_list , name="drinks_list"),
    path("sweet_dish/", sweet_dish, name="sweet_dish" ),
    path("desserts_list/", desserts_list, name="desserts_list"),
    path("create_food/", create_food , name="create_food" ),
    path("create_drink/", create_drink, name="create_drink"),
    path("create_dessert/", create_dessert, name="create_dessert"),
    path("add_food/", add_food , name="add_food"),           
    path("update_food/<int:pk>/", update_food, name= "update_food"),
    path("update_drink/<int:pk>/", update_drink, name="update_drink"),  
    path("update_dessert/<int:pk>/", update_dessert, name="update_dessert"),  
    path("delete_food/<int:pk>/", Delete_food.as_view() , name= "delete_food"),
    path("delete_dessert/<int:pk>/", Delete_dessert.as_view() , name= "delete_dessert"),
    path("delete_drink/<int:pk>/", Delete_drink.as_view() , name= "delete_drink"),    
]