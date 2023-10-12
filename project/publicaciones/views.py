from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from . import models, forms
class PublicacionesList(ListView):
    model = models.Publicaciones
    
    def get_queryset(self):
        consulta = self.request.GET.get("buscar")
    
        if consulta:       
            object_list = models.Publicaciones.objects.filter(titulo__icontains=consulta)
        else:        
            object_list = models.Publicaciones.objects.all()    
        return object_list
    
class PublicacionesDetail(DetailView):
    model = models.Publicaciones
    
    
class PublicacionesCreate(CreateView):
    model = models.Publicaciones
    form_class = forms.PublicacionesForm
    success_url = reverse_lazy("publicaciones:publicaciones_list")
    
class PublicacionesUpdate(UpdateView):
    model = models.Publicaciones
    form_class = forms.PublicacionesForm
    success_url = reverse_lazy("publicaciones:publicaciones_list")
    
class PublicacionesDelete(DeleteView):
    model = models.Publicaciones
    success_url = reverse_lazy("publicaciones:publicaciones_list")

