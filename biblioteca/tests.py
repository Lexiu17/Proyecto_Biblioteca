from django.contrib.auth.models import User
from django.core.management import call_command
from django.test import TestCase
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
