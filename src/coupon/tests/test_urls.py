from django.test import SimpleTestCase
from django.urls import resolve, reverse

from coupon import views


class TestUrls(SimpleTestCase):

    def test_list_coupon_url(self):
        url = reverse('coupon:list_coupon')
        self.assertEquals(resolve(url).func.view_class, views.ShowCouponListView)

    def test_add_to_cart_url(self):
        url = reverse('coupon:add_to_cart')
        self.assertEquals(resolve(url).func.view_class, views.AddToCartCoupon)

    def test_create_coupon_url(self):
        url = reverse('coupon:create_coupon')
        self.assertEquals(resolve(url).func.view_class, views.CreateCouponView)

    def test_update_coupon_url(self):
        url = reverse('coupon:update_coupon', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.UpdateCouponView)

    def test_delete_coupon_url(self):
        url = reverse('coupon:delete_coupon', kwargs={'pk': 1})
        self.assertEquals(resolve(url).func.view_class, views.DeleteCouponView)

    def test_send_to_email_url(self):
        url = reverse('coupon:send_to_email')
        self.assertEquals(resolve(url).func.view_class, views.SendCouponToEmail)
