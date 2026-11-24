from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from biblioteca.forms import prestamoForm
from biblioteca.models import prestamo as Prestamo

def prestamo_list(request):
    prestamos = Prestamo.objects.all()
    return render(request, 'biblioteca/prestamos/prestamo_list.html',
                  {'prestamos': prestamos})

def prestamo_detail(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    return render(request, 'biblioteca/prestamos/prestamo_detail.html',
                  {'prestamo': prestamo})

def prestamo_create(request):
    if request.method == 'POST':
        form = prestamoForm(request.POST)
        if form.is_valid():
            prestamo = form.save(commit=False)
            if request.user.is_authenticated:
                prestamo.creado_por = request.user
            prestamo.save()
            form.save_m2m()
            messages.success(request, 'Préstamo creado exitosamente.')
            return redirect('prestamo_list')
    else:
        form = prestamoForm()
    return render(request, 'biblioteca/prestamos/formulario.html', {'form': form})

def prestamo_update(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        form = prestamoForm(request.POST, instance=prestamo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Préstamo actualizado exitosamente.')
            return redirect('prestamo_list')
    else:
        form = prestamoForm(instance=prestamo)
    return render(request, 'biblioteca/prestamos/formulario.html', {'form': form})

def prestamo_delete(request, prestamo_id):
    prestamo = get_object_or_404(Prestamo, pk=prestamo_id)
    if request.method == 'POST':
        prestamo.delete()
        messages.success(request, 'Préstamo eliminado exitosamente.')
        return redirect('prestamo_list')
    return render(request, 'biblioteca/prestamos/prestamo_confirm_delete.html',
                  {'prestamo': prestamo})

