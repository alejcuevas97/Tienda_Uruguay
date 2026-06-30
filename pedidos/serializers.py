from rest_framework import serializers
from .models import Pedido, ItemPedido

class ItemPedidoSerializers(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()
    
    class Meta:
        model= ItemPedido
        fields= ["id","pedido","regalo", "cantidad","subtotal"
                ]
        
class PedidoSerializers(serializers.ModelSerializer):
    subtotal = ItemPedidoSerializers(many=True, source="itempedido_set", read_only=True)
    
    class Meta:
        model= Pedido
        fields= ["id","usuario","fecha", "total","items"
                ]        
        
        