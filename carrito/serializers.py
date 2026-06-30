from rest_framework import serializers
from .models import ItemCarrito

class ItemCarritoSerializers(serializers.ModelSerializer):
    subtotal = serializers.ReadOnlyField()
    class Meta:
        model= ItemCarrito
        fields= ["id","usuario","regalo", "cantidad","subtotal"
                ]
        
        