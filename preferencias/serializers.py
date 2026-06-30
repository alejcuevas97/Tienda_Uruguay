from rest_framework import serializers
from .models import Preferencia

class PreferenciaSerializers(serializers.ModelSerializer):
    class Meta:
        model= Preferencia
        fields= ["id","usuario","color", "perfume","sabor","rango_min","rango_max"
                ]
        
        