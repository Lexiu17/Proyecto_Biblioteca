from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
from django.urls import reverse

from biblioteca.models import Autor, Editorial, Libro, Prestamo


class CargarDatosCommandTests(TestCase):
    def test_creates_expected_demo_users_and_book_owners(self):
        call_command('cargar_datos')

        superuser = User.objects.get(username='nenata')
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.check_password('12345'))

        reader = User.objects.get(username='lector1')
        self.assertTrue(reader.check_password('lect12345'))
        self.assertTrue(reader.groups.filter(name='consultores').exists())

        self.assertEqual(
            Libro.objects.get(isbn='978-0000000028').creado_por,
            reader,
        )
        self.assertEqual(
            Libro.objects.get(isbn='978-0000000042').creado_por,
            reader,
        )


class ModelStringRepresentationTests(TestCase):
    def test_author_and_publisher_use_their_names(self):
        author = Autor(nombre='Gabriel García Márquez')
        publisher = Editorial(nombre='Editorial Sur')

        self.assertEqual(str(author), 'Gabriel García Márquez')
        self.assertEqual(str(publisher), 'Editorial Sur')

    def test_book_and_loan_use_readable_names(self):
        book = Libro(titulo='Cien años de soledad')
        loan = Prestamo(nombre_lector='Ana', libro=book)

        self.assertEqual(str(book), 'Cien años de soledad')
        self.assertEqual(str(loan), 'Ana - Cien años de soledad')


class AuthorPublisherCrudViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser(
            username='catalog_admin',
            email='catalog_admin@example.com',
            password='test-password',
        )
        self.client.force_login(self.user)

    def test_author_create_and_update(self):
        response = self.client.get(reverse('autor_create'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('autor_create'), {
            'nombre': 'Isabel Allende',
            'nacionalidad': 'Chilena',
            'fecha_nacimiento': '1942-08-02',
        })
        self.assertRedirects(response, reverse('autor_list'))
        author = Autor.objects.get(nombre='Isabel Allende')

        response = self.client.get(reverse('autor_detail', args=[author.pk]))
        self.assertContains(response, reverse('autor_update', args=[author.pk]))

        response = self.client.post(
            reverse('autor_update', args=[author.pk]),
            {
                'nombre': 'Isabel Allende Llona',
                'nacionalidad': 'Chilena',
                'fecha_nacimiento': '1942-08-02',
            },
        )
        self.assertRedirects(response, reverse('autor_list'))
        author.refresh_from_db()
        self.assertEqual(author.nombre, 'Isabel Allende Llona')

    def test_publisher_create_and_update(self):
        response = self.client.get(reverse('editorial_create'))
        self.assertEqual(response.status_code, 200)

        response = self.client.post(reverse('editorial_create'), {
            'nombre': 'Editorial Sur',
            'pais': 'Argentina',
            'fundacion': '1931-01-01',
        })
        self.assertRedirects(response, reverse('editorial_list'))
        publisher = Editorial.objects.get(nombre='Editorial Sur')

        response = self.client.get(
            reverse('editorial_detail', args=[publisher.pk]),
        )
        self.assertContains(
            response,
            reverse('editorial_update', args=[publisher.pk]),
        )

        response = self.client.post(
            reverse('editorial_update', args=[publisher.pk]),
            {
                'nombre': 'Editorial Sur Editada',
                'pais': 'Argentina',
                'fundacion': '1931-01-01',
            },
        )
        self.assertRedirects(response, reverse('editorial_list'))
        publisher.refresh_from_db()
        self.assertEqual(publisher.nombre, 'Editorial Sur Editada')

    def test_catalog_creation_requires_permissions(self):
        reader = User.objects.create_user(
            username='reader',
            password='test-password',
        )
        self.client.force_login(reader)

        self.assertEqual(
            self.client.get(reverse('autor_create')).status_code,
            403,
        )
        self.assertEqual(
            self.client.get(reverse('editorial_create')).status_code,
            403,
        )

        self.assertNotContains(
            self.client.get(reverse('autor_list')),
            reverse('autor_create'),
        )
        self.assertNotContains(
            self.client.get(reverse('editorial_list')),
            reverse('editorial_create'),
        )


class DetailViewNotFoundTests(TestCase):
    def test_missing_book_returns_404(self):
        response = self.client.get('/libros/999/')

        self.assertEqual(response.status_code, 404)

    def test_missing_author_returns_404(self):
        response = self.client.get('/autores/999/')

        self.assertEqual(response.status_code, 404)

    def test_missing_publisher_returns_404(self):
        response = self.client.get('/editoriales/999/')

        self.assertEqual(response.status_code, 404)

    def test_missing_loan_returns_404(self):
        response = self.client.get('/prestamos/999/')

        self.assertEqual(response.status_code, 404)
