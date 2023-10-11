from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models, forms
class CasasComunidadList(ListView):
    model = models.CasasComunidad
    
class CasasComunidadDetail(DetailView):
    model = models.CasasComunidad
    template_name = "comunidad/casascomunidad_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        casa = context['object']
        miembros = casa.miembro_set.all()
        context['miembros'] = miembros
        return context
    
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
    
    ###########################################################
    
class MiembroList(ListView):
    model = models.Miembro
    
class MiembroDetail(DetailView):
    model = models.Miembro
    
class MiembroCreate(CreateView):
    model = models.Miembro
    form_class = forms.MiembroForm
    success_url = reverse_lazy("comunidad:miembro_list")
    
class MiembroUpdate(UpdateView):
    model = models.Miembro
    form_class = forms.MiembroForm
    success_url = reverse_lazy("comunidad:miembro_list")
    
class MiembroDelete(DeleteView):
    model = models.Miembro
    success_url = reverse_lazy("comunidad:miembro_list")
    

    