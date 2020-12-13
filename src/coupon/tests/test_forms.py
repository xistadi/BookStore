from django.test import SimpleTestCase
from coupon import forms


class TestForms(SimpleTestCase):

    def test_create_coupon_form_valid_data(self):
        """test create coupon form with valid data"""
        form = forms.CreateCouponForm(data={
            'name': 'test',
            'percent': 5,
            'active': True,
        })
        self.assertTrue(form.is_valid())

    def test_create_coupon_form_no_data(self):
        """test create coupon form with no data"""
        form = forms.CreateCouponForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 2)
