from django.urls import path
from django.views.generic import TemplateView
from . import views

app_name = "publicaciones"

urlpatterns = [
    path("", TemplateView.as_view(template_name="publicaciones/index.html"), name="index"),
    path("publicaciones_list/", views.PublicacionesList.as_view(), name="publicaciones_list"),
    path("publicaciones_detail/<int:pk>/", views.PublicacionesDetail.as_view(), name="publicaciones_detail"),
    path("publicaciones_create/", views.PublicacionesCreate.as_view(), name="publicaciones_create"),
    path("publicaciones_delete/<int:pk>/", views.PublicacionesDelete.as_view(), name="publicaciones_delete"),
    path("publicaciones_update/<int:pk>/", views.PublicacionesUpdate.as_view(), name="publicaciones_update"),    
]