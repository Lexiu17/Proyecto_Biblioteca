from django.urls import path
from biblioteca.views import autor_list, autor_detail

urlpatterns = [
    path('autores/', autor_list, name='autor_list'),
    path('autores/<int:autor_id>/', autor_detail, name='autor_detail'),
]