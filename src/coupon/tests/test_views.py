from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import Group
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission

from coupon import models
from cart.views import create_cart
from cart import models as models_cart

User = get_user_model()

class TestViews(TestCase):

    def setUp(self):
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
        self.cart = create_cart(self.user, self.session)
        self.coupon = models.Coupon.objects.create(name='unittest', percent=10, active=True)
        self.list_coupon_url = reverse('coupon:list_coupon')
        self.add_to_cart_url = reverse('coupon:add_to_cart')
        self.create_coupon_url = reverse('coupon:create_coupon')
        self.update_coupon_url = reverse('coupon:update_coupon', kwargs={'pk': 1})
        self.delete_coupon_url = reverse('coupon:delete_coupon', kwargs={'pk': 1})
        self.send_to_email_url = reverse('coupon:send_to_email')

    def test_list_coupon_view(self):
        """test coupon list"""
        response = self.client.get(self.list_coupon_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'coupon/coupon_list.html')

    def test_add_to_cart_view(self):
        """test add coupon to card view"""
        cart = create_cart(self.user, self.session)
        response = self.client.post(self.add_to_cart_url, {'promo': 'unittest', 'cart_id': 2})
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models_cart.Cart.objects.last().coupon_percent, self.coupon.percent)

    def test_create_coupon_view(self):
        """test coupon create"""
        response = self.client.post(self.create_coupon_url, {
            'name': 'test',
            'percent': 10,
            'active': True
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Coupon.objects.last().name, 'test')
        self.assertEqual(models.Coupon.objects.last().percent, 10)

    def test_update_coupon_view(self):
        """test update coupon"""
        response = self.client.post(self.update_coupon_url, {
            'name': 'testU',
            'percent': 10,
            'active': True
        })
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Coupon.objects.last().name, 'testU')

    def test_delete_coupon_view(self):
        """test delete coupon"""
        response = self.client.post(self.delete_coupon_url)
        self.assertEquals(response.status_code, 302)
        self.assertEqual(models.Coupon.objects.all().count(), 0)

    def test_send_to_email_view(self):
        """test send to email coupon"""
        response = self.client.post(self.send_to_email_url, {'email': 'test@gmail.com'})
        self.assertEquals(response.status_code, 302)
