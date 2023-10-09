from django.shortcuts import render

from . import models
# Create your views here.
def index(request):
    publicacion = models.Publicaciones.objects.all()
    
    return render(request, "publicaciones/index.html", {"publicaciones":publicacion})

