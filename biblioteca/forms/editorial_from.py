from django import forms
from biblioteca.models import editorial

class editorialForm(forms.ModelForm):
    class Meta:
        model = editorial
        fields = ['nombre', 
                  'pais', 
                  'fundacion']
        widgets = {
            'fundacion': forms.DateInput(attrs={'type': 'date'}, 
                                         format='%Y-%m-%d'),
        }