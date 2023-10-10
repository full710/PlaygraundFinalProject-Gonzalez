from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "comunidad"

urlpatterns = [
    path("", TemplateView.as_view(template_name="comunidad/index.html"), name="index"),
    path("miembro_create/", views.MiembroCreate.as_view(), name="miembro_create"),
    path("miembro_list/", views.MiembroList.as_view(), name="miembro_list"),
    path("miembro_detail/<int:pk>", views.MiembroDetail.as_view(), name="miembro_detail"),
    path("miembro_delete/<int:pk>", views.MiembroDelete.as_view(), name="miembro_delete"),
    path("miembro_update/<int:pk>", views.MiembroUpdate.as_view(), name="miembro_update"),
    path("casascomunidad/list/", views.CasasComunidadList.as_view(), name="casascomunidad_list"),
    path("casascomunidad/detail/<int:pk>", views.CasasComunidadDetail.as_view(), name="casascomunidad_detail"),
    path("casascomunidad/create/", views.CasasComunidadCreate.as_view(), name="casascomunidad_create"),
    path("casascomunidad/update/<int:pk>/", views.CasasComunidadUpdate.as_view(), name="casascomunidad_update"),
    path("casascomunidad/delete/<int:pk>/", views.CasasComunidadDelete.as_view(), name="casascomunidad_delete"),


    
]