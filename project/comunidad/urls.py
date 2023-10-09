from django.urls import path, include
from . import views

app_name = "comunidad"

urlpatterns = [
    path("", views.index, name="index"),
    path("crear_miembro/", views.crear, name="crear_miembro")
]