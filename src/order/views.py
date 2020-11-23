from django.shortcuts import render
from django.views.generic import edit
from . import models, forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from cart import views as cart_views


class OrderUpdateView(edit.UpdateView):
    form_class = forms.OrderUpdateForm
    template_name = 'order/update_order.html'
    success_url = reverse_lazy('myaccount')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delivery_status = 2
        cart_views.create_cart(self.request.user, self.request.session)
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form))

    def get_queryset(self):
        return models.Order.objects
