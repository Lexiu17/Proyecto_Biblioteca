from django import forms
from biblioteca.models import prestamo

class prestamoForm(forms.ModelForm):
    class Meta:
        model = prestamo
        fields = ['libro', 
                  'nombre_lector', 
                  'fecha_prestamo', 
                  'fecha_devolucion',
                  'estado']
        widgets = {
            'fecha_prestamo': forms.DateInput(attrs={'type': 'date'}, 
                                              format='%Y-%m-%d'),
            'fecha_devolucion': forms.DateInput(attrs={'type': 'date'}, 
                                                 format='%Y-%m-%d'),
        }

