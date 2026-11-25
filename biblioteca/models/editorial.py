from django.db import models
from django.urls import reverse

class editorial(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    pais = models.CharField(max_length=60)
    fundacion = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    def get_absolute_url(self):
        return reverse('editorial_detail', args=[self.pk])

    class Meta:
        ordering = ['nombre']
        verbose_name = 'Editorial'
        verbose_name_plural = 'Editoriales'
