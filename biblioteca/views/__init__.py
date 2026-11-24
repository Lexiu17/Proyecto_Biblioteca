from django.shortcuts import render
from biblioteca.views.home_views import home
from biblioteca.views.editorial_views import editorial_list, editorial_detail
from biblioteca.views.autor_views import autor_list, autor_detail
from biblioteca.views.libro_views import (
    libro_list, libro_detail, libro_create, libro_update, libro_delete,
)
from biblioteca.views.prestamo_views import (
    prestamo_list, prestamo_detail, prestamo_create, prestamo_update, prestamo_delete,
)