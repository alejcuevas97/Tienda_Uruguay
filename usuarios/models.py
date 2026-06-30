from django.db import models
from django.contrib.auth.models import User


class Usuario(models.Model):
    telefono = models.CharField(max_length=20, blank=True)
    direccion = models.TextField(blank=True)
    
    
