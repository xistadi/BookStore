from django.shortcuts import render
from django.views.generic import edit
from . import models, forms
from django.core.exceptions import ImproperlyConfigured


class OrderUpdateView(edit.UpdateView):
    form_class = forms.OrderUpdateForm
    template_name = 'order/update_order.html'

    def get_queryset(self):
        return models.Order.objects
