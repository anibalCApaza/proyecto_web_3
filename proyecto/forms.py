from django import forms
from .models import Team
from django.core.exceptions import ValidationError
from .models import Task

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'description', 'start_date', 'end_date']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 4}),
            'start_date': forms.DateInput(attrs={'type': 'date'}),
            'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'name': 'Nombre del proyecto',
            'description': 'Descripción',
            'start_date': 'Fecha de inicio',
            'end_date': 'Fecha de fin',
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get("start_date")
        end_date = cleaned_data.get("end_date")

        if start_date and end_date and end_date < start_date:
            raise ValidationError("La fecha de fin no puede ser anterior a la de inicio.")