from rest_framework import serializers
from .models import Usuario

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model= Usuario
        fields= ["id","username","email", "telefono","direccion"
                ]
        
        