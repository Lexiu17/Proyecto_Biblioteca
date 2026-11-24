from django.db import models
from django.urls import reverse

class autor(models.Model):
    nombre = models.CharField (max_length=100)
    nacionalidad = models.CharField (max_length=60)
    fecha_nacimiento = models.DateField (null=True, blank=True)

def __str__(self):
    return self.nombre

def get_absolute_url(self):
    return reverse('autor-detail', args=[str(self.id)])

class Meta:
    ordering = ['nombre']
    verbose_name = 'Autor'
    verbose_name_plural = 'Autores'


