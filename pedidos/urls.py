from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet,ItemPedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)
router.register(r'item-pedido', ItemPedidoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
