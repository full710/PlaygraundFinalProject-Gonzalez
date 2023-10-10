from django.contrib import admin

# Register your models here.
from . import models
admin.site.site_title = "Comunidad"

admin.site.register(models.CasasComunidad)
class CasasComunidadAdmin(admin.ModelAdmin):
    list_display = ("nombre_casa","descripcion",)
    search_fields = ("nombre_casa",)
    list_filter = ("nombre_casa",)
    ordering = ("nombre_casa",)
    
admin.site.register(models.Miembro)    
class MiembroAdmin(admin.ModelAdmin):
    list_display = ("nombre","apellido","nacimiento","profesion")
    search_fields = ("nombre",)
    list_filter = ("nombre",)
    ordering = ("nombre",)
