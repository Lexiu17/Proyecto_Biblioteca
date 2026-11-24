from django import forms
from biblioteca.models import libro

class libroForm(forms.ModelForm):
    class Meta:
        model = libro
        fields = ['titulo', 
                  'isbn', 
                  'año_publicacion', 
                  'precio', 
                  'editorial', 
                  'autores']
        widgets = {
            'autores': forms.CheckboxSelectMultiple(),
        }

