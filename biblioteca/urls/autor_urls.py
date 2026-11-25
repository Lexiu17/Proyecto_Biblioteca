from django.urls import path
from biblioteca.views import (
    autor_list, autor_detail, autor_create, autor_update,
)

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/crear/', autor_create, name='autor_create'),
    path('autores/<int:autor_id>/', autor_detail, name='autor_detail'),
    path('autores/<int:autor_id>/editar/', autor_update, name='autor_update'),
]