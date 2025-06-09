from django import forms
from .models import Etiqueta

class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta
        fields = ['nombre', 'relevancia']
        