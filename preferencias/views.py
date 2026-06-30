from django.shortcuts import render
from .forms import PreferenciaForm
from .models import Preferencia
from .services import sugerir_regalos
from rest_framework import viewsets
from .serializers import PreferenciaSerializers

# Create your views here.
class PreferenciaViewSet(viewsets.ModelViewSet):
    queryset = Preferencia.objects.all()
    serializer_class = PreferenciaSerializers
    
    
# Create your views here.
def configurar_regalos(request):
    if request.method == "POST":
        form = PreferenciaForm(request.POST)
        if form.is_valid():
            preferencias = form.save(commit=False)
            preferencias.usuario = request.user
            preferencias.save()
            
            regalos_sugeridos = sugerir_regalos(preferencias)
            return render(request,"sugerencias.html",{"regalos":regalos_sugeridos})
        else:
            form = PreferenciaForm()
        return render(request, "configurar.html", {"form":form})    