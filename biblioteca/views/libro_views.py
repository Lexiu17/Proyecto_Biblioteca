from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render

from biblioteca.forms import libroForm
from biblioteca.models import libro


def libro_list(request):
    libros = libro.objects.all()
    return render(request, 'biblioteca/libros/libro_list.html',
                  {'libros': libros})


def libro_detail(request, libro_id):
    libro = get_object_or_404(libro, pk=libro_id)
    return render(request, 'biblioteca/libros/libro_detail.html',
                  {'libro': libro})


@login_required
@permission_required('biblioteca.add_libro', raise_exception=True)
def libro_create(request):
    if request.method == 'POST':
        form = libroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            libro.creado_por = request.user
            libro.save()
            form.save_m2m()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('libro_list')
    else:
        form = libroForm()
    return render(request, 'biblioteca/libros/formulario.html', {'form': form})


@login_required
@permission_required('biblioteca.change_libro', raise_exception=True)
def libro_update(request, libro_id):
    libro = get_object_or_404(libro, pk=libro_id)

    # Regla de propiedad: solo edita quien lo creó, o quien tenga el permiso especial
    if not request.user.has_perm('biblioteca.editar_todos_libros'):
        if libro.creado_por != request.user:
            raise PermissionDenied

    if request.method == 'POST':
        form = libroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('libro_list')
    else:
        form = libroForm(instance=libro)
    return render(request, 'biblioteca/libros/formulario.html', {'form': form})


@login_required
@permission_required('biblioteca.delete_libro', raise_exception=True)
def libro_delete(request, libro_id):
    libro = get_object_or_404(libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('libro_list')
    return render(request, 'biblioteca/libros/libro_confirm_delete.html',
                  {'libro': libro})
