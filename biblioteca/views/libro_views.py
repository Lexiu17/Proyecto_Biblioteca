from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from biblioteca.forms import libroForm
from biblioteca.models import libro as Libro
from django.contrib.auth.decorators import login_required

def libro_list(request):
    libros = Libro.objects.all()
    return render(request, 'biblioteca/libros/libro_list.html',
                  {'libros': libros})


def libro_detail(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    return render(request, 'biblioteca/libros/libro_detail.html',
                  {'libro': libro})

@login_required
def libro_create(request):
    if request.method == 'POST':
        form = libroForm(request.POST)
        if form.is_valid():
            libro = form.save(commit=False)
            if request.user.is_authenticated:
                libro.creado_por = request.user
            libro.save()
            form.save_m2m()
            messages.success(request, 'Libro creado exitosamente.')
            return redirect('libro_list')
    else:
        form = libroForm()
    return render(request, 'biblioteca/libros/formulario.html', {'form': form})


def libro_update(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        form = libroForm(request.POST, instance=libro)
        if form.is_valid():
            form.save()
            messages.success(request, 'Libro actualizado exitosamente.')
            return redirect('libro_list')
    else:
        form = libroForm(instance=libro)
    return render(request, 'biblioteca/libros/formulario.html', {'form': form})


def libro_delete(request, libro_id):
    libro = get_object_or_404(Libro, pk=libro_id)
    if request.method == 'POST':
        libro.delete()
        messages.success(request, 'Libro eliminado exitosamente.')
        return redirect('libro_list')
    return render(request, 'biblioteca/libros/libro_confirm_delete.html',
                  {'libro': libro})