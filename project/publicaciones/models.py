from django.db import models

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    cantidad = models.IntegerField(null=True, blank=True)
    precio = models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    email_contacto = models.EmailField(null=True,blank=True)
    telefono_contacto = models.IntegerField(null=True,blank=True)
    
    class Meta:
        verbose_name = "Publicación"
        verbose_name_plural = "Publicaciones"
        
    def __str__(self):
        return self.titulo