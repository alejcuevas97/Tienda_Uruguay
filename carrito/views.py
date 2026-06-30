from django.shortcuts import render, redirect
from .models import ItemCarrito
from regalos.models import Regalo
from rest_framework import viewsets
from .models import ItemCarrito
from .serializers import ItemCarritoSerializers

# Create your views here.
class CarritoViewSet(viewsets.ModelViewSet):
    queryset = ItemCarrito.objects.all()
    serializer_class = ItemCarritoSerializers
    
    
# Create your views here.
def ver_carrito(request):
    items = ItemCarrito.objects.filter(usuario=request.user)
    total = sum([item.subtotal() for item in items])
    return render(request, "carrito.html", {"items":items, "total": total})

def agregar_carrito(request, regalo_id):
    regalo = Regalo.objects.get(id=regalo_id)
    item, created = ItemCarrito.objects.get_or_create(usuario=request.user, regalo=regalo)
    if not created:
        item.cantidad += 1
        item.save()
    return redirect ("ver_carrito")

def eliminar_carrito(request, item_id):
    item = ItemCarrito.objects.get(id=item_id)
    item.delete()
    return redirect("ver_carrito")   