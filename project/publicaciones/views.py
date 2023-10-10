from django.shortcuts import render, redirect

from . import models, forms
# Create your views here.
def index(request):
    publicacion = models.Publicaciones.objects.all()
    
    return render(request, "publicaciones/index.html", {"publicaciones":publicacion})

def crear(request):
    if request.method == "POST":
        form = forms.PublicacionesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("publicaciones:index")
    else:
        form = forms.PublicacionesForm()
    return render(request, "publicaciones/crear_publicacion.html", {"form":form})

