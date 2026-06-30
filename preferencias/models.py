from django.db import models
from django.contrib.auth.models import User

#Usuario = get_user_model

class Preferencia(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    color = models.CharField(max_length=50, blank=True)
    perfume = models.CharField(max_length=100, blank=True)
    sabor = models.CharField(max_length=100, blank=True)
    otros = models.TextField(blank=True)
    rango_min = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    rango_max = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def __str__(self):
        return f"Preferencias de {self.usuario.username}"

