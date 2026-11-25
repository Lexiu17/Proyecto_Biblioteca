from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from biblioteca.forms import PrestamoForm
from biblioteca.models import Prestamo


def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'biblioteca/prestamos/prestamo_list.html',
                  {'prestamos': prestamos})


def prestamo_detail(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    return render(request, 'biblioteca/prestamos/prestamo_detail.html',
                  {'prestamo': prestamo})


@login_required
@permission_required('biblioteca.add_prestamo', raise_exception=True)
def prestamo_create(request):
    if request.method == 'POST':
        form = PrestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            prestamo.creado_por = request.user
            prestamo.save()
            messages.success(request, 'Préstamo creado exitosamente.')
            return redirect('prestamo_list')
    else:
        form = PrestamoForm()
    return render(request, 'biblioteca/prestamos/formulario.html', {'form': form})


@login_required
@permission_required('biblioteca.change_prestamo', raise_exception=True)
def prestamo_update(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        form = PrestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo actualizado exitosamente.')
            return redirect('prestamo_list')
    else:
        form = PrestamoForm(instance=prestamo)
    return render(request, 'biblioteca/prestamos/formulario.html', {'form': form})


@login_required
@permission_required('biblioteca.delete_prestamo', raise_exception=True)
def prestamo_delete(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        prestamo.delete()
        messages.success(request, 'Préstamo eliminado exitosamente.')
        return redirect('prestamo_list')
    return render(request, 'biblioteca/prestamos/prestamo_confirm_delete.html',
                  {'prestamo': prestamo})