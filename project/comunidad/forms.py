from django import forms

from . import models

class MiembroForm(forms.ModelForm):
    class Meta:
        model = models.Miembro
        fields = ["nombre","apellido","nacimiento","profesion","casa_comarca"]
        
class CasasComunidadForm(forms.ModelForm):
    class Meta:
        model = models.CasasComunidad
        fields = ["nombre_casa","descripcion"]