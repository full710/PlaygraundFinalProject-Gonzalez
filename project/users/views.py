from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import RegistroForm, InicioSesionForm, EditarPerfilForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


class RegistroView(CreateView):
    form_class = RegistroForm
    success_url = reverse_lazy('home:index')
    template_name = 'registro.html'

class InicioSesionView(LoginView):
    form_class = InicioSesionForm        
    template_name = 'inicio-sesion.html'
    
@login_required
def perfil(request):
    user = request.user 
    return render(request, 'users/perfil.html', {'user': user})

@login_required
def editar_perfil(request):
    if request.method == 'POST':
        form = EditarPerfilForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:perfil')
    else:
        form = EditarPerfilForm(instance=request.user)
    return render(request, 'users/editar_perfil.html', {'form': form})

def cerrar_sesion(request):
    logout(request)
    return redirect('home:index')