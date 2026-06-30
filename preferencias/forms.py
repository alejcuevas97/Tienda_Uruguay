from django import forms
from .models import Preferencia

class PreferenciaForm(forms.ModelForm):
    class Meta:
        model = Preferencia
        fields = ['color', 'perfume','sabor','rango_min','rango_max']