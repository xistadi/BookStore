from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from cart import views
from cart import models
from products.models import Book
from references import models as references_models
from order.models import Order

User = get_user_model()


class TestModels(TestCase):

    def setUp(self):
        """setUp for cart test models"""
        group = Group.objects.get(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        self.user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        self.session = self.client.session
        self.cart = views.create_cart(self.user, self.session)
        self.author = references_models.Author.objects.create(name='unittest')
        self.series = references_models.Series.objects.create(name='unittest')
        self.genre = references_models.Genre.objects.create(name='unittest')
        self.publisher = references_models.Publisher.objects.create(name='unittest')
        self.book = Book.objects.create(name='unittest', price=1, series=self.series, binding=1, book_format='',
                                          isbn='', age_limit='', publisher=self.publisher, active=True)
        self.book_in_cart = models.BookInCart.objects.create(cart=self.cart, book=self.book, quantity=1,
                                                             price=self.book.price)

    def test_total_price_one_book_models(self):
        """test total price one book models"""
        total_price = self.cart.total_price()
        self.assertEqual(total_price, 1)

    def test_total_price_two_books_models(self):
        """test total price two books models"""
        book = Book.objects.create(name='unittest', price=1, series=self.series, binding=1, book_format='',
                                   isbn='', age_limit='', publisher=self.publisher, active=True)
        book_in_cart = models.BookInCart.objects.create(cart=self.cart, book=book, quantity=1,
                                                        price=self.book.price)
        total_price = self.cart.total_price()
        self.assertEqual(total_price, 2)

    def test_construct_price_models(self):
        """test construct price models"""
        book = Book.objects.create(name='unittest', price=1, series=self.series, binding=1, book_format='',
                                   isbn='', age_limit='', publisher=self.publisher, active=True)
        book_in_cart = models.BookInCart.objects.create(cart=self.cart, book=book, quantity=2,
                                                        price=self.book.price)
        price = book_in_cart.construct_price()
        self.assertEqual(price, 2)
