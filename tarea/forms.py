from django import forms
from .models import Etiqueta, Tarea


class TareaForm(forms.ModelForm):
    
    # Definimos las opciones directamente en el formulario
    ESTADO_OPCIONES = [
        ('Pendiente', 'Pendiente'),
        ('En proceso', 'En proceso'),
        ('Completo', 'Completo'),
    ]
    
    # Sobreescribimos el campo 'estado' en el formulario
    estado = forms.ChoiceField(
        choices=ESTADO_OPCIONES,
        widget=forms.Select(attrs={'class': 'form-select'})
    )
    
    class Meta:
        model = Tarea
        fields = [
            "nombre",
            "descripcion",
            "estado",
        ]  # excluimos 'creado_en' porque se asigna automáticamente

        widgets = {
            "nombre": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "Nombre de la tarea"}
            ),
            "descripcion": forms.Textarea(
                attrs={"class": "form-control", "placeholder": "Descripción"}
            ),
            # 
        }


class EtiquetaForm(forms.ModelForm):
    class Meta:
        model = Etiqueta

        fields = ["nombre", "relevancia"]
