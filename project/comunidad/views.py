from django.shortcuts import render, redirect

from . import models, forms
# Create your views here.
def index(request):
    casa = models.CasasComunidad.objects.all()
    
    return render(request, "comunidad/index.html", {"casas":casa})

def crear(request):
    if request.method == "POST":
        form = forms.MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comunidad:index")
    else:
        form = forms.MiembroForm()
    return render(request, "comunidad/crear_miembro.html", {"form":form})

def crear_casa(request):
    if request.method == "POST":
        form = forms.CasaComarcaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comunidad:index")
    else:
        form = forms.CasaComarcaForm()
    return render(request, "comunidad/crear_casa.html", {"form":form})

def lista_completa(request):
    miembro = models.Miembro.objects.all()
    return render (request, "comunidad/lista_completa.html", {"miembros":miembro})
    