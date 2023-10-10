from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models, forms
class CasasComunidadList(ListView):
    model = models.CasasComunidad
    
class CasasComunidadDetail(DetailView):
    model = models.CasasComunidad
    
class CasasComunidadCreate(CreateView):
    model = models.CasasComunidad
    form_class = forms.CasasComunidadForm
    success_url = reverse_lazy("comunidad:casascomunidad_list")
    
class CasasComunidadUpdate(UpdateView):
    model = models.CasasComunidad
    form_class = forms.CasasComunidadForm
    success_url = reverse_lazy("comunidad:casascomunidad_list")
    
class CasasComunidadDelete(DeleteView):
    model = models.CasasComunidad
    success_url = reverse_lazy("comunidad:casascomunidad_list")
    

def crear(request):
    if request.method == "POST":
        form = forms.MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("comunidad:index")
    else:
        form = forms.MiembroForm()
    return render(request, "comunidad/crear_miembro.html", {"form":form})



def lista_completa(request):
    miembro = models.Miembro.objects.all()
    return render (request, "comunidad/lista_completa.html", {"miembros":miembro})
    