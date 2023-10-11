from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    numero_telefono = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.username