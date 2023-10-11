from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm
from .models import CustomUser


class RegistroForm(UserCreationForm):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    email = forms.EmailField()
    numero_telefono = forms.CharField(max_length=15)
    fecha_nacimiento = forms.DateField()

    class Meta:
        model = CustomUser
        fields = ('nombre', 'apellido', 'username', 'email', 'numero_telefono', 'fecha_nacimiento', 'password1', 'password2')

class InicioSesionForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')

class EditarPerfilForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('nombre', 'apellido', 'email', 'numero_telefono', 'fecha_nacimiento')