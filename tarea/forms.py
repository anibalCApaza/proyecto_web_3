from django import forms
from .models import Etiqueta, Tarea


class TareaForm(forms.ModelForm):
    class Meta:
        model = Tarea
        fields = [
            "nombre",
            "descripcion",
            "estado",
            "proyecto",
        ]  # excluimos 'creado_en' porque se asigna automáticamente

        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de la tarea"}
            ),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción"}
            ),
            "estado": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Estado"}
            ),
            "proyecto": forms.Select(attrs={"class": "form-control"}),
        }


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta

        fields = ["nombre", "relevancia"]
