from django.urls import path, include
from . import views

app_name = "comunidad"

urlpatterns = [
    path("", views.index, name="index"),
]