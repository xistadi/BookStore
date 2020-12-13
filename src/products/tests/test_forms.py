from django.test import TestCase

from products import forms
from references import models as references_models


class TestForms(TestCase):

    def setUp(self):
        self.author = references_models.Author.objects.create(name='unittest')
        self.series = references_models.Series.objects.create(name='unittest')
        self.genre = references_models.Genre.objects.create(name='unittest')
        self.publisher = references_models.Publisher.objects.create(name='unittest')

    def test_create_book_form_valid_data(self):
        """test create book form with valid data"""
        form = forms.CreateBookForm(data={
            'name': 'test',
            'price': 12,
            'series': 1,
            'year': 1998,
            'page': 1,
            'binding': 'test',
            'book_format': 'test',
            'isbn': 'test',
            'weight': 1,
            'age_limit': 'test',
            'publisher': 1,
            'number_of_books': 1,
            'active': True,
            'number_of_orders': 1,
            'avr_rating': 1,
            'author': ['1'],
            'genre': ['1'],
        })
        self.assertTrue(form.is_valid())

    def test_create_book_form_no_data(self):
        """test create book form with no data"""
        form = forms.CreateBookForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 16)

