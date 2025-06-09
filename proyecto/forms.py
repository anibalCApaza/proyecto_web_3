from django import forms
from .models import Proyecto


class ProyectoForm(forms.ModelForm):
    fecha_ini = forms.DateField(
        label="Fecha inicio",
        widget=forms.DateInput(attrs={"type": "date"}),
    )
    fecha_fin = forms.DateField(
        label="Fecha fin",
        widget=forms.DateInput(attrs={"type": "date"}),
    )

    class Meta:
        model = Proyecto
        fields = ["nombre", "descripcion", "fecha_ini", "fecha_fin"]
        # Excluimos creado_en y usuario_crea, se auto asignarán
