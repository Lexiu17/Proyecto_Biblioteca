from django.urls import path
from biblioteca.views import (
    prestamo_list, prestamo_detail, prestamo_create, prestamo_update, prestamo_delete,
)

urlpatterns = [
    path('prestamos/', prestamo_list, name='prestamo_list'),
    path('prestamos/crear/', prestamo_create, name='prestamo_create'),
    path('prestamos/<int:prestamo_id>/', prestamo_detail, name='prestamo_detail'),
    path('prestamos/<int:prestamo_id>/editar/', prestamo_update, name='prestamo_update'),
    path('prestamos/<int:prestamo_id>/eliminar/', prestamo_delete, name='prestamo_delete'),
]
