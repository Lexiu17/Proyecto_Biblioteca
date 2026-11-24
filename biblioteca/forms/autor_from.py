from django import forms
from biblioteca.models import autor

class autorForm(forms.ModelForm):
    class Meta:
        model = autor
        fields = ['nombre', 
                  'nacionalidad', 
                  'fecha_nacimiento']
        widgets = {
            'fecha_nacimiento': forms.DateInput(attrs={'type': 'date'}, 
                                                format='%Y-%m-%d'),
        }