from django.db import models

# Create your models here.
class Publicaciones(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=300)
    cantidad = models.IntegerField(null=True)
    precio = models.DecimalField(max_digits=5,decimal_places=2,null=True)
    email_contacto = models.EmailField(null=True)
    telefono_contacto = models.IntegerField(null=True)
    
    
    def __str__(self):
        return self.titulo