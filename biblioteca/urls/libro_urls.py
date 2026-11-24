from django.urls import path
from biblioteca.views import (
    libro_list, libro_detail, libro_create, libro_update, libro_delete,
)

urlpatterns = [
    path('libros/', libro_list, name='libro_list'),
    path('libros/crear/', libro_create, name='libro_create'),
    path('libros/<int:libro_id>/', libro_detail, name='libro_detail'),
    path('libros/<int:libro_id>/editar/', libro_update, name='libro_update'),
    path('libros/<int:libro_id>/eliminar/', libro_delete, name='libro_delete'),
]

