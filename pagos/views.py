from django.shortcuts import render
from carrito.models import ItemCarrito

# Create your views here.
def checkout(request):
    items = ItemCarrito.objects.filter(usuario=request.user)
    total = sum([item.subtotal() for item in items])
    return render (request, "checkout.html", {"items":items, "total":total})

def pago_exitoso(request):
    return render(request, "pago_exitoso.html")

def pago_fallido(request):
    return render(request, "pago_fallido.html")