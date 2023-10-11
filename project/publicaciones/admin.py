from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_title = "Publicaciones"
admin.site.register(models.Publicaciones)

class PublicacionAdmin(admin.ModelAdmin):
    list_display = ("titulo","descripcion","cantidad","precio","email_contacto","telefono_contacto",)
    search_fields = ("titulo",)
    list_filter = ("titulo",)
    ordering = ("titulo",)
    date_hierarchy = "fecha_actualizacion"
    
