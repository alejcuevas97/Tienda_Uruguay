from django.shortcuts import render
from .models import Pedido
from rest_framework import viewsets
from .models import Pedido,ItemPedido
from .serializers import PedidoSerializers,ItemPedidoSerializers

# Create your views here.
class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializers
class ItemPedidoViewSet(viewsets.ModelViewSet):
    queryset = ItemPedido.objects.all()
    serializer_class = ItemPedidoSerializers    

# Create your views here.
def historial_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user)
    return render(request, "pedidos.html", {"pedidos":pedidos})