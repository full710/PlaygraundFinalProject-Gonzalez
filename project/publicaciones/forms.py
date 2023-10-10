from django import forms

from . import models

class PublicacionesForm(forms.ModelForm):
    class Meta:
        model = models.Publicaciones
        fields = ["titulo","descripcion","cantidad","precio","email_contacto","telefono_contacto"]