from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .libro import libro

class prestamo(models.Model):

    class EstadoPrestamo(models.TextChoices):
        ACTIVO = 'activo', 'Activo'
        DEVUELTO = 'devuelto', 'Devuelto'
        ATRASADO = 'atrasado', 'Atrasado'

    libro = models.ForeignKey(
        libro,
        on_delete=models.PROTECT,
        related_name='prestamos',
    )
    nombre_lector = models.CharField(max_length=100)
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField()
    estado = models.CharField(
        max_length=10,
        choices=EstadoPrestamo.choices,
        default=EstadoPrestamo.ACTIVO,
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='prestamos_creados',
    )

def __str__(self):
    return self.nombre_lector + ' - ' + self.libro.titulo

def get_absolute_url(self):
    return reverse('prestamo_detail', args=[self.pk])

class Meta:
    verbose_name = 'Préstamo'
    verbose_name_plural = 'Préstamos'
    ordering = ['-fecha_prestamo']

    