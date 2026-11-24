from django.contrib import admin
from biblioteca.models import editorial, autor, libro, prestamo

admin.site.register(editorial)
admin.site.register(autor)
admin.site.register(libro)
admin.site.register(prestamo)
