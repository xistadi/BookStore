from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from products import models
from references import models as references_models

User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        group = Group.objects.get(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        user.is_superuser = True
        user.is_staff = True
        user.save()
        self.author = references_models.Author.objects.create(name='unittest')
        self.series = references_models.Series.objects.create(name='unittest')
        self.genre = references_models.Genre.objects.create(name='unittest')
        self.publisher = references_models.Publisher.objects.create(name='unittest')
        book = models.Book.objects.create(name='unittest', price=1, series=self.series, binding=1, book_format='',
                                          isbn='', age_limit='', publisher=self.publisher, active=True)
        book.genre.set([1])
        book.author.set([1])
        self.reference_url = reverse('products:book_list')
        self.book_by_pk_url = reverse('products:book_by_pk', kwargs={'pk': 1})
        self.book_create_url = reverse('products:create_new_book')
        self.book_delete_url = reverse('products:delete_book_by_pk', kwargs={'pk': 1})
        self.search_results_url = reverse('products:search_results')

    def test_book_list_view(self):
        """test book list"""
        response = self.client.get(self.reference_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/book_list.html')

    def test_book_by_pk_view(self):
        """test book by pk"""
        response = self.client.get(self.book_by_pk_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/book.html')

    def test_book_create_view(self):
        """test book create"""
        response = self.client.post(self.book_create_url, {
            'name': 'test1',
            'price': 0,
            'series': self.series.id,
            'publisher': self.publisher.id,
            'binding': '1',
            'book_format': '1',
            'isbn': '1',
            'age_limit': '1',
            'author': ['1'],
            'genre': ['1'],
            'year': 1,
            'page': 1,
            'weight': 1,
            'number_of_books': 1,
            'active': 1,
            'number_of_orders': 1,
            'avr_rating': 0
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Book.objects.last().name, 'test1')

    def test_book_update_view(self):
        """test book update"""
        response = self.client.post(f'/books/update/{models.Book.objects.last().pk}/', {
            'name': 'testunittes',
            'price': 0,
            'series': self.series.id,
            'publisher': self.publisher.id,
            'binding': '1',
            'book_format': '1',
            'isbn': '1',
            'age_limit': '1',
            'author': ['1'],
            'genre': ['1'],
            'year': 1,
            'page': 1,
            'weight': 1,
            'number_of_books': 1,
            'active': 1,
            'number_of_orders': 1,
            'avr_rating': 0
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Book.objects.last().name, 'testunittes')

    def test_book_delete_view(self):
        """test book delete"""
        response = self.client.post(self.book_delete_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Book.objects.all().count(), 0)

    def test_search_results_view(self):
        """test search results"""
        response = self.client.get(self.search_results_url, {'search': 'testunittes'})
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/book_search_list.html')
