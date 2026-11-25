from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .editorial import editorial
from .autor import autor

class libro(models.Model):
    titulo = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20, unique=True)
    año_publicacion = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    editorial = models.ForeignKey(
        editorial,
        on_delete=models.PROTECT,
        related_name='libros',
    )
    autores = models.ManyToManyField(
        autor,
        related_name='libros',
    )
    creado_por = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='libros_creados',
    )

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('libro_detail', args=[self.pk])

    class Meta:
        verbose_name = 'Libro'
        verbose_name_plural = 'Libros'
        ordering = ['titulo']
        permissions = [
            ('editar_todos_libros', 'Puede editar libros creados por otros'),
        ]