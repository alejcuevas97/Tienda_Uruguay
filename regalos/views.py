from django.shortcuts import render
from .models import Regalo
from rest_framework import viewsets
from .models import Regalo
from .serializers import RegaloSerializers

# Create your views here.
class RegaloViewSet(viewsets.ModelViewSet):
    queryset = Regalo.objects.all()
    serializer_class = RegaloSerializers
    
    
# Create your views here.
def lista_regalos(request):
    regalos = Regalo.objects.all()
    return render(request, "sugerencias.html", {"regalos":regalos})
