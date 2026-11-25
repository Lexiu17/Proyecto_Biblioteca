from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Crea los grupos administradores y consultores con sus permisos'

    def handle(self, *args, **options):
        modelos = ['editorial', 'autor', 'libro', 'prestamo']

        # Grupo administradores: todo en las cuatro entidades
        permisos_admin = ['editar_todos_libros']
        for modelo in modelos:
            for accion in ['add', 'change', 'delete', 'view']:
                permisos_admin.append(accion + '_' + modelo)

        administradores, creado = Group.objects.get_or_create(name='administradores')
        administradores.permissions.set(
            Permission.objects.filter(
                codename__in=permisos_admin,
                content_type__app_label='biblioteca',
            )
        )

        # Grupo consultores: ver todo, crear libros y editar los suyos
        permisos_consultor = [
            'view_editorial',
            'view_autor',
            'view_libro',
            'view_prestamo',
            'add_libro',
            'change_libro',
        ]

        consultores, creado = Group.objects.get_or_create(name='consultores')
        consultores.permissions.set(
            Permission.objects.filter(
                codename__in=permisos_consultor,
                content_type__app_label='biblioteca',
            )
        )

        print('Grupos listos: administradores con', administradores.permissions.count(),
              'permisos y consultores con', consultores.permissions.count(), 'permisos.')