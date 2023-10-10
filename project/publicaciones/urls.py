from django.urls import path, include
from . import views

app_name = "publicaciones"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear_publicacion/", views.crear, name="crear_publicacion"),
    
]