from django.conf import settings
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render
from django.utils.http import url_has_allowed_host_and_scheme
from django.views.decorators.http import require_POST
from django.contrib.auth.models import Group

from biblioteca.forms import RegistroForm


def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            grupo = Group.objects.filter(name='consultores').first()
            if grupo:
                usuario.groups.add(grupo)
            messages.success(request, 'Cuenta creada exitosamente. Ahora inicia sesión.')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'biblioteca/auth/registro.html', {'form': form})

def iniciar_sesion(request):
    siguiente = request.GET.get('next', '')
    if request.method == 'POST':
        siguiente = request.POST.get('next', '')
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            messages.success(request, 'Bienvenido, ' + usuario.username + '.')
            if siguiente and url_has_allowed_host_and_scheme(siguiente, allowed_hosts={request.get_host()}):
                return redirect(siguiente)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = AuthenticationForm()
    return render(request, 'biblioteca/auth/login.html',
                  {'form': form, 'next': siguiente})


@require_POST
def cerrar_sesion(request):
    logout(request)
    messages.success(request, 'Sesión cerrada correctamente.')
    return redirect(settings.LOGOUT_REDIRECT_URL)