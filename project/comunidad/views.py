from django.shortcuts import render

from . import models
# Create your views here.
def index(request):
    miembro = models.Miembro.objects.all()
    
    return render(request, "comunidad/index.html", {"miembros":miembro})