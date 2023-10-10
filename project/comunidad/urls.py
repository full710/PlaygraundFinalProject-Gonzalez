from django.urls import path, include
from . import views

app_name = "comunidad"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear_miembro/", views.crear, name="crear_miembro"),
    path("crear_casa/", views.crear_casa, name="crear_casa"),
    path("lista_completa/", views.lista_completa, name="lista_completa"),
]