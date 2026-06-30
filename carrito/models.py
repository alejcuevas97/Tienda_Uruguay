from django.db import models
from django.contrib.auth.models import User
from regalos.models import Regalo

#creo una instancia de Usuario
#Usuario = get_user_model


#creando los modelos de tablas para el carrito
class ItemCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    regalo = models.ForeignKey(Regalo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)
    
    def subtotal(self):
        return self.regalo.precio * self.cantidad
