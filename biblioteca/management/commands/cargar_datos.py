from datetime import date

from django.contrib.auth.models import Group, User
from django.core.management import call_command
from django.core.management.base import BaseCommand

from biblioteca.models import Editorial, Autor, Libro, Prestamo


class Command(BaseCommand):
    help = 'Carga usuarios de prueba y 5 registros por tabla'

    def handle(self, *args, **options):
        # Primero los grupos, para poder asignarlos
        call_command('crear_grupos')

        # ---------- Usuarios de prueba ----------
        if not User.objects.filter(username='nenata').exists():
            User.objects.create_superuser('nenata', 'nenata@biblioteca.com', '12345')

        admin1, creado = User.objects.get_or_create(
            username='admin1',
            defaults={'email': 'admin1@biblioteca.com'},
        )
        admin1.set_password('Admin12345')
        admin1.is_staff = True
        admin1.save()
        admin1.groups.add(Group.objects.get(name='administradores'))

        lector1, creado = User.objects.get_or_create(
            username='lector1',
            defaults={'email': 'lector1@biblioteca.com'},
        )
        lector1.set_password('lect12345')
        lector1.save()
        lector1.groups.add(Group.objects.get(name='consultores'))

        # ---------- Editoriales ----------
        editoriales = [
            ('Planeta', 'España', date(1949, 1, 1)),
            ('Penguin Random House', 'Estados Unidos', date(2013, 7, 1)),
            ('Alfaguara', 'España', date(1964, 1, 1)),
            ('Fondo de Cultura Económica', 'México', date(1934, 9, 3)),
            ('Anagrama', 'España', date(1969, 1, 1)),
        ]
        for datos in editoriales:
            Editorial.objects.get_or_create(
                nombre=datos[0],
                defaults={'pais': datos[1], 'fundacion': datos[2]},
            )

        # ---------- Autores ----------
        autores = [
            ('Gabriel García Márquez', 'Colombiana', date(1927, 3, 6)),
            ('Isabel Allende', 'Chilena', date(1942, 8, 2)),
            ('Jorge Luis Borges', 'Argentina', date(1899, 8, 24)),
            ('Mario Vargas Llosa', 'Peruana', date(1936, 3, 28)),
            ('Julio Cortázar', 'Argentina', date(1914, 8, 26)),
        ]
        for datos in autores:
            Autor.objects.get_or_create(
                nombre=datos[0],
                defaults={'nacionalidad': datos[1], 'fecha_nacimiento': datos[2]},
            )

        # ---------- Libros (los ISBN son de prueba) ----------
        # (titulo, isbn, año, precio, editorial, [autores], usuario creador)
        libros = [
            ('Cien años de soledad', '978-0000000011', 1967, '18.50', 'Alfaguara',
             ['Gabriel García Márquez'], 'admin1'),
            ('La casa de los espíritus', '978-0000000028', 1982, '16.90', 'Planeta',
             ['Isabel Allende'], 'lector1'),
            ('Ficciones', '978-0000000035', 1944, '14.00', 'Fondo de Cultura Económica',
             ['Jorge Luis Borges'], 'admin1'),
            ('La ciudad y los perros', '978-0000000042', 1963, '15.75', 'Alfaguara',
             ['Mario Vargas Llosa'], 'lector1'),
            ('Antología del cuento latinoamericano', '978-0000000059', 1975, '22.00', 'Anagrama',
             ['Jorge Luis Borges', 'Julio Cortázar'], 'admin1'),
        ]
        for datos in libros:
            libro, creado = Libro.objects.get_or_create(
                isbn=datos[1],
                defaults={
                    'titulo': datos[0],
                    'año_publicacion': datos[2],
                    'precio': datos[3],
                    'editorial': Editorial.objects.get(nombre=datos[4]),
                    'creado_por': User.objects.get(username=datos[6]),
                },
            )
            for nombre_autor in datos[5]:
                libro.autores.add(Autor.objects.get(nombre=nombre_autor))

        # ---------- Préstamos ----------
        # (titulo del libro, lector, fecha préstamo, fecha devolución, estado)
        prestamos = [
            ('Cien años de soledad', 'Ana Torres', date(2026, 11, 2), date(2026, 11, 16),
             Prestamo.EstadoPrestamo.DEVUELTO),
            ('La casa de los espíritus', 'Luis Mena', date(2026, 11, 10), None,
             Prestamo.EstadoPrestamo.ACTIVO),
            ('Ficciones', 'Carla Vega', date(2026, 10, 15), None,
             Prestamo.EstadoPrestamo.ATRASADO),
            ('La ciudad y los perros', 'Pedro Soto', date(2026, 11, 18), None,
             Prestamo.EstadoPrestamo.ACTIVO),
            ('Antología del cuento latinoamericano', 'María Paredes', date(2026, 11, 5), date(2026, 11, 20),
             Prestamo.EstadoPrestamo.DEVUELTO),
        ]
        for datos in prestamos:
            Prestamo.objects.get_or_create(
                libro=Libro.objects.get(titulo=datos[0]),
                nombre_lector=datos[1],
                defaults={
                    'fecha_prestamo': datos[2],
                    'fecha_devolucion': datos[3],
                    'estado': datos[4],
                    'creado_por': admin1,
                },
            )

        print('Datos cargados:')
        print('Editoriales:', Editorial.objects.count())
        print('Autores:', Autor.objects.count())
        print('Libros:', Libro.objects.count())
        print('Prestamos:', Prestamo.objects.count())
        print('Usuarios de prueba: nenata, admin1, lector1')