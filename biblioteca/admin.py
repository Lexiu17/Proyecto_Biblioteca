from django.contrib import admin
from biblioteca.models import Editorial, Autor, Libro, Prestamo


@admin.register(Editorial)
class EditorialAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'pais', 'fundacion')
    list_filter = ('pais',)
    search_fields = ('nombre', 'pais')


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'nacionalidad', 'fecha_nacimiento')
    list_filter = ('nacionalidad',)
    search_fields = ('nombre', 'nacionalidad')


@admin.register(Libro)
class LibroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'isbn', 'año_publicacion', 'precio', 'editorial', 'creado_por')
    list_filter = ('editorial', 'año_publicacion', 'creado_por')
    search_fields = ('titulo', 'isbn')
    filter_horizontal = ('autores',)


@admin.register(Prestamo)
class PrestamoAdmin(admin.ModelAdmin):
    list_display = ('nombre_lector', 'libro', 'fecha_prestamo', 'fecha_devolucion', 'estado', 'creado_por')
    list_filter = ('estado', 'fecha_prestamo')
    search_fields = ('nombre_lector', 'libro__titulo')