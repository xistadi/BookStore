from django.shortcuts import render
from django.views.generic import edit
from . import models, forms


class OrderUpdateView(edit.UpdateView):
    form_class = forms.OrderUpdateForm
    template_name = 'order/update_order.html'

    def get_object(self):
        return self.request.user
