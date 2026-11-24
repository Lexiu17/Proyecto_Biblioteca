from django.urls import path
from biblioteca.views import editorial_list, editorial_detail

urlpatterns = [
    path('editoriales/', editorial_list, name='editorial_list'),
    path('editoriales/<int:editorial_id>/', editorial_detail, name='editorial_detail'),
]