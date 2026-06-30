from rest_framework import serializers
from .models import Regalo

class RegaloSerializers(serializers.ModelSerializer):
    class Meta:
        model= Regalo
        fields= ["id","nombre","descripcion", "precio","imagen"
                ]
        
        