from django.contrib import admin

# Register your models here.
from . import models

admin.site.register(models.CasasComunidad)
admin.site.register(models.Miembro)
