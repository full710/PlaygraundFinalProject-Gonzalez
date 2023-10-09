from django.shortcuts import render, redirect

from . import models, forms
# Create your views here.
def index(request):
    miembro = models.Miembro.objects.all()
    
    return render(request, "comunidad/index.html", {"miembros":miembro})

def crear(request):
    if request.method == "POST":
        form = forms.MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comunidad:index")
    else:
        form = forms.MiembroForm()
    return render(request, "comunidad/crear_miembro.html", {"form":form})