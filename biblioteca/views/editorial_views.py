from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.shortcuts import get_object_or_404, redirect, render

from biblioteca.forms import EditorialForm
from biblioteca.models import Editorial


def editorial_list(request):
    editoriales = Editorial.objects.all()
    return render(request, 'biblioteca/editoriales/editorial_list.html',
                  {'editoriales': editoriales})


def editorial_detail(request, editorial_id):
    editorial = get_object_or_404(Editorial, pk=editorial_id)
    return render(request, 'biblioteca/editoriales/editorial_detail.html',
                  {'editorial': editorial})


@login_required
@permission_required('biblioteca.add_editorial', raise_exception=True)
def editorial_create(request):
    if request.method == 'POST':
        form = EditorialForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editorial creada exitosamente.')
            return redirect('editorial_list')
    else:
        form = EditorialForm()
    return render(request, 'biblioteca/editoriales/formulario.html', {'form': form})


@login_required
@permission_required('biblioteca.change_editorial', raise_exception=True)
def editorial_update(request, editorial_id):
    editorial = get_object_or_404(Editorial, pk=editorial_id)
    if request.method == 'POST':
        form = EditorialForm(request.POST, instance=editorial)
        if form.is_valid():
            form.save()
            messages.success(request, 'Editorial actualizada exitosamente.')
            return redirect('editorial_list')
    else:
        form = EditorialForm(instance=editorial)
    return render(request, 'biblioteca/editoriales/formulario.html', {'form': form})