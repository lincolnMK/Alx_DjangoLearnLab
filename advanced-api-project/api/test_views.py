from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from api.models import Author, Book
from datetime import date

class BaseAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # Authenticated user
        self.user = User.objects.create_user(
            username='testuser',
            password='password123'
        )

        # Author
        self.author = Author.objects.create(name="George Orwell")

        # Book
        self.book = Book.objects.create(
            title="1984",
            author=self.author,
            publication_year=1949  # ✅ integer
        )

# ----------------------
# BookList Tests
# ----------------------
class BookListTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('book-list')

    def test_list_books_public(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_unauthenticated(self):
        data = {
            "title": "Animal Farm",
            "author": self.author.id,
            "publication_year": 1945
        }
        response = self.client.post(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_create_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Animal Farm",
            "author": self.author.id,
            "publication_year": 1945
        }
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_books_by_publication_year(self):
        response = self.client.get(self.url, {'publication_year': 1949})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        response = self.client.get(self.url, {'search': '1984'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        response = self.client.get(self.url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
class BookDetailTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('book-detail', args=[self.book.id])

    def test_retrieve_book(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_book_unauthenticated(self):
        data = {
            "title": "Updated Title",
            "author": self.author.id,
            "publication_year": 1950
        }
        response = self.client.put(self.url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Updated Title",
            "author": self.author.id,
            "publication_year": 1950
        }
        response = self.client.put(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Title")
        self.assertEqual(self.book.publication_year, 1950)

    def test_delete_book_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

# ----------------------
# Author Tests
# ----------------------
class AuthorTests(BaseAPITestCase):
    def setUp(self):
        super().setUp()
        self.list_url = reverse('author-list')
        self.detail_url = reverse('author-detail', args=[self.author.id])

    def test_list_authors(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_author_authenticated(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.post(self.list_url, {"name": "Aldous Huxley"}, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_delete_author_unauthenticated(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


# ----------------------
# AuthorBooks Custom View Test
# ----------------------
class AuthorBooksTests(BaseAPITestCase):
    def test_get_books_by_author(self):
        url = reverse('author-books', args=[self.author.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

# ----------------------
# Auth-only CreateBook & UpdateBook Views
# ----------------------
class AuthenticatedBookActionsTests(BaseAPITestCase):
    def test_create_book_requires_auth(self):
        url = reverse('book-create')
        response = self.client.post(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_book_requires_auth(self):
        url = reverse('book-update', args=[self.book.id])
        response = self.client.put(url, {})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
