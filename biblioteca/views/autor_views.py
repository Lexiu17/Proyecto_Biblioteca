from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from biblioteca.forms import AutorForm
from biblioteca.models import Autor


def autor_list(request):
    autores = Autor.objects.all()
    return render(request, 'biblioteca/autores/autor_list.html',
                  {'autores': autores})


def autor_detail(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    return render(request, 'biblioteca/autores/autor_detail.html',
                  {'autor': autor})


@login_required
@permission_required('biblioteca.add_autor', raise_exception=True)
def autor_create(request):
    if request.method == 'POST':
        form = AutorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor creado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm()
    return render(request, 'biblioteca/autores/formulario.html', {'form': form})


@login_required
@permission_required('biblioteca.change_autor', raise_exception=True)
def autor_update(request, autor_id):
    autor = get_object_or_404(Autor, pk=autor_id)
    if request.method == 'POST':
        form = AutorForm(request.POST, instance=autor)
        if form.is_valid():
            form.save()
            messages.success(request, 'Autor actualizado exitosamente.')
            return redirect('autor_list')
    else:
        form = AutorForm(instance=autor)
    return render(request, 'biblioteca/autores/formulario.html', {'form': form})