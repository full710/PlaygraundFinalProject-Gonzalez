from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import path, include
from . import views

app_name = "home"

urlpatterns = [
    path("", views.index, name="index"),
    path("abaut/", views.abaut, name="abaut")
]

urlpatterns += staticfiles_urlpatterns()