from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "comunidad"

urlpatterns = [
    path("", TemplateView.as_view(template_name="comunidad/index.html"), name="index"),
    path("crear_miembro/", views.crear, name="crear_miembro"),
    path("lista_completa/", views.lista_completa, name="lista_completa"),
    path("casascomunidad/list/", views.CasasComunidadList.as_view(), name="casascomunidad_list"),
    path("casascomunidad/detail/<int:pk>", views.CasasComunidadDetail.as_view(), name="casascomunidad_detail"),
    path("casascomunidad/create/", views.CasasComunidadCreate.as_view(), name="casascomunidad_create"),
    path("casascomunidad/update/<int:pk>/", views.CasasComunidadUpdate.as_view(), name="casascomunidad_update"),
    path("casascomunidad/delete/<int:pk>/", views.CasasComunidadDelete.as_view(), name="casascomunidad_delete"),


    
]