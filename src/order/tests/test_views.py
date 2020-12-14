from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from order import views
from order import models
from cart import views as cart_views
from cart import models as cart_models
from myauth import models as myauth_models
from products.models import Book
from references import models as references_models

User = get_user_model()


class TestViews(TestCase):

    def setUp(self):
        """setUp for order test views"""
        group = Group.objects.get(name='Customers')
        permissions = Permission.objects.all()
        group.permissions.set(permissions)
        group.save()
        self.user = User.objects.create_user('unittest', password='unittest')
        self.client.login(username="unittest", password="unittest")
        self.user.is_superuser = True
        self.user.is_staff = True
        self.user.save()
        self.profile = self.user.profile
        myauth_models.ProfileAddress.objects.create(profile=self.profile, country='unit_test', city='unit_test',
                                                    index='unit_test', address1='unit_test', address2='unit_test')
        self.session = self.client.session
        self.cart = cart_views.create_cart(self.user, self.session)
        self.author = references_models.Author.objects.create(name='unittest')
        self.series = references_models.Series.objects.create(name='unittest')
        self.genre = references_models.Genre.objects.create(name='unittest')
        self.publisher = references_models.Publisher.objects.create(name='unittest')
        self.book = Book.objects.create(name='unittest', price=1, series=self.series, binding=1, book_format='',
                                        isbn='', age_limit='', publisher=self.publisher, active=True)
        self.book_in_cart = cart_models.BookInCart.objects.create(cart=self.cart, book=self.book, quantity=1,
                                                             price=self.book.price)
        self.order = models.Order.objects.create(cart=self.cart, delivery_status=1, comment='test', type_of_payment='1')
        self.update_order_url = reverse('order:update_order')
        self.order_list_url = reverse('order:order_list')

    def test_update_order_view(self):
        """test order update view"""
        cart = cart_views.create_cart(self.user, self.session)
        response = self.client.post(self.update_order_url, {'address': 1, 'cart_id': 1, 'paymentMethod': 'test'})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Order.objects.last().type_of_payment, 'test')
        self.assertEqual(models.Order.objects.last().address_in_order.last().country,
                         myauth_models.ProfileAddress.objects.last().country)

    def test_view_order_view(self):
        """test view order view"""
        response = self.client.get('/order/update_status/1')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/update_status_order.html')

    def test_update_status_order_view(self):
        """test update status order view"""
        response = self.client.post('/order/update_status/1', {'delivery_status': 3})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Order.objects.all().last().delivery_status, '3')

    def test_order_list_view(self):
        """test order list view"""
        response = self.client.get(self.order_list_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'order/order_list.html')

    def test_update_manager_view(self):
        """test update order for manager"""
        response = self.client.post('/order/update_manager/1', {'delivery_status': 2, 'comment': 'test_update_manager'})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Order.objects.all().last().comment, 'test_update_manager')

    def test_cancel_order_view(self):
        """test cancel order view"""
        response = self.client.post('/order/cancel_order/1')
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Order.objects.all().last().delivery_status, '3')
