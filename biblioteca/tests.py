from django.test import TestCase


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
