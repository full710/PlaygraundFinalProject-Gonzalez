from django.shortcuts import render
from django.http import HttpResponse
from publicaciones.models import Publicaciones
# Create your views here.

def index(request):
    publicacion = Publicaciones.objects.all()  # Consulta todas las publicaciones en la base de datos
    return render(request, 'home/index.html', {'publicaciones': publicacion})
    

def abaut(request):
    return render(request, "home/abaut.html")

