from django.contrib import admin
from django.urls import path, include
from lunch.views import  search_food, start
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('admin/', admin.site.urls),   
    path("search_food/" , search_food , name ="search_food"),
    path("", start, name= "start"),
    path("lunch/" , include("lunch.urls")),
    path("users/" , include("users.urls")),
    
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
