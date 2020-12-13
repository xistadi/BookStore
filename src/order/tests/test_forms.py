from django.test import SimpleTestCase
from order import forms


class TestForms(SimpleTestCase):

    def test_order_update_form_valid_data(self):
        """test update order form with valid data"""
        form = forms.OrderUpdateForm(data={
            'comment': 'test',
        })
        self.assertTrue(form.is_valid())

    def test_order_update_form_no_data(self):
        """test update order form with no data"""
        form = forms.OrderUpdateForm(data={})
        self.assertTrue(form.is_valid())
        self.assertEquals(len(form.errors), 0)

    def test_order_delivery_status_update_form_valid_data(self):
        """test update order delivery status form with valid data"""
        form = forms.OrderDeliveryStatusUpdateForm(data={
            'delivery_status': '1',
        })
        self.assertTrue(form.is_valid())

    def test_order_delivery_status_update_form_no_data(self):
        """test update order delivery status form with no data"""
        form = forms.OrderDeliveryStatusUpdateForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)

    def test_order_update_for_managers_form_valid_data(self):
        """test update order form for managers with valid data"""
        form = forms.OrderUpdateForManagersForm(data={
            'comment': 'test',
            'delivery_status': '1',
        })
        self.assertTrue(form.is_valid())

    def test_order_update_for_managers_form_no_data(self):
        """test update order form for managers with no data"""
        form = forms.OrderUpdateForManagersForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEquals(len(form.errors), 1)
