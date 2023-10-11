from django.db import models

# Create your models here.
class CasasComunidad(models.Model):
    nombre_casa = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=500)
    
    def __str__(self):
        return self.nombre_casa
    
    class Meta:
        verbose_name = "Casa"
        verbose_name_plural = "Casas"
        
class Miembro(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacimiento = models.DateField(null=True)
    profesion = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    casa_comarca = models.ForeignKey(CasasComunidad, on_delete=models.SET_NULL,null=True,blank=True, verbose_name="Hogar en la comarca")
    
    class Meta:
        verbose_name = "Miembro"
        verbose_name_plural = "Miembros"
    
    def __str__(self):
        return f"{self.nombre.title()} {self.apellido.title()}"
    
