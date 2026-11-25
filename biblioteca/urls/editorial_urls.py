from django.urls import path
from biblioteca.views import (
    editorial_list, editorial_detail, editorial_create, editorial_update,
)

urlpatterns = [
    path('editoriales/', editorial_list, name='editorial_list'),
    path('editoriales/crear/', editorial_create, name='editorial_create'),
    path('editoriales/<int:editorial_id>/', editorial_detail, name='editorial_detail'),
    path('editoriales/<int:editorial_id>/editar/', editorial_update, name='editorial_update'),
]