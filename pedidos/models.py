from django.db import models
from django.contrib.auth.models import User
from regalos.models import Regalo

#creo una instancia de Usuario
#Usuario = get_user_model

#creando los modelos de tablas para realizar los pedidos
class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    
    def calcualr_total(self):
        items = self.itempedido_set.all()
        self.total = sum([item.subtotal() for item in items])
        self.save()

class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    regalo = models.ForeignKey(Regalo, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)
    
    def subtotal(self):
        return self.regalo.precio * self.cantidad        