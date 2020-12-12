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


class TestViews(TestCase):

    def setUp(self):
        """setUp for cart test views"""
        group = Group.objects.create(name='Customers')
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
        self.book_in_cart = models.BookInCart.objects.create(cart=self.cart, book=self.book, quantity=1, price=self.book.price)
        self.cart_index_url = reverse('cart:cart_index')
        self.cart_update_url = reverse('cart:update_cart')

    def test_create_cart_view(self):
        """test create cart"""
        views.create_cart(self.user, self.session)
        self.assertEqual(self.session.get('cart_id'), 2)
        self.assertEqual(models.Cart.objects.count(), 2)

    def test_cart_index_view(self):
        """test cart view"""
        response = self.client.get(self.cart_index_url)
        self.assertEqual(models.Cart.objects.count(), 2)
        self.assertEquals(response.status_code, 200)

    def test_update_cart_view(self):
        """test update quantity book int cart"""
        cart = views.create_cart(self.user, self.session)
        book_in_cart = models.BookInCart.objects.create(cart=cart, book=self.book, quantity=1, price=self.book.price)
        response = self.client.post(self.cart_update_url, {f'{book_in_cart.pk}': 99, 'submit_button': 'edit',
                                                           'cart_id': cart.pk})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(cart.books.first().quantity, 99)

    def test_checkout_cart_view(self):
        """test checkout cart"""
        cart = views.create_cart(self.user, self.session)
        book_in_cart = models.BookInCart.objects.create(cart=cart, book=self.book, quantity=1, price=self.book.price)
        response = self.client.post(self.cart_update_url, {f'{book_in_cart.pk}': 99, 'cart_id': cart.pk})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.last().cart, cart)

    def test_add_to_cart_book_view(self):
        """test add to cart book view"""
        response = self.client.get(self.cart_index_url, {'book': self.book.pk})
        self.assertEquals(response.status_code, 200)
        self.assertEqual(models.Cart.objects.last().books.count(), 1)
