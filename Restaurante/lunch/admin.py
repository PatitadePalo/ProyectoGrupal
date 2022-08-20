from django.contrib import admin
from lunch.models import principal, drink, dessert

@admin.register(principal)
class principal_admin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "celiac"]

@admin.register(drink)
class drink_admin(admin.ModelAdmin):
    list_display = ["name", "price", "description"]


@admin.register(dessert)
class dessert_admin(admin.ModelAdmin):
    list_display = ["name", "price", "description", "celiac"]