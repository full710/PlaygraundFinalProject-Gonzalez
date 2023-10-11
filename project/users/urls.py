from django.urls import path
from django.views.generic import TemplateView
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth import views as auth_views

app_name = "users"

urlpatterns = [
    path("", TemplateView.as_view(template_name="users/index.html"), name="index"),
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('registro/', views.RegistroView.as_view(template_name="users/registro.html"), name='registro'),
    path('inicio-sesion/', views.InicioSesionView.as_view(template_name="users/inicio-sesion.html"), name='inicio-sesion'),
    path('perfil/', views.perfil, name='perfil'),
    path('editar_perfil/', views.editar_perfil, name='editar_perfil'),
    path('cerrar-sesion/', views.cerrar_sesion, name='logout')
]