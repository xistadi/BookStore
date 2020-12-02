from django.views import generic
from . import models, forms
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.core.mail import send_mail
from django.contrib import messages
from django.contrib.auth.models import User

from cart import views as cart_views
from cart import models as cart_models


class OrderUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Создаем заказ"""
    form_class = forms.OrderUpdateForm
    template_name = 'order/update_order.html'
    success_url = reverse_lazy('myaccount')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delivery_status = 2
        address_in_order = models.AddressInOrder.objects.create(order=self.object)
        address_id = self.request.POST.get('address')
        address_from_user = self.request.user.profile.profile_address.filter(pk=address_id).first()
        address_in_order.country = address_from_user.country
        address_in_order.city = address_from_user.city
        address_in_order.index = address_from_user.index
        address_in_order.address1 = address_from_user.address1
        address_in_order.address2 = address_from_user.address2
        address_in_order.save()
        type_of_payment_from_post = self.request.POST.get('paymentMethod')
        self.object.type_of_payment = type_of_payment_from_post
        cart_views.create_cart(self.request.user, self.request.session)
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            for manager in User.objects.filter(is_staff=True).all():
                send_mail(
                    'New order',
                    'Here is the message.',
                    'xistadifirstsitetest@gmail.com',
                    [f'{manager.email}'],
                    fail_silently=False,
                )
            messages.success(request, "Отлично! Заказ оформлен!")
            for book_from_cart in self.object.cart.books.all():
                book_from_cart.book.number_of_orders += 1
                book_from_cart.book.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form))

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        cart = cart_models.Cart.objects.filter(pk=cart_id).first()
        return cart.order


class UpdateStatusOrderView(LoginRequiredMixin, generic.edit.UpdateView):
    """Обновляем статус заказа для покупателя"""
    form_class = forms.OrderDeliveryStatusUpdateForm
    template_name = 'order/update_status_order.html'
    success_url = reverse_lazy('myaccount')

    def get_queryset(self):
        return models.Order.objects


class UpdateStatusOrderForManagerView(PermissionRequiredMixin, generic.edit.UpdateView):
    """Обновляем статус заказа для менеджера"""
    form_class = forms.OrderDeliveryStatusUpdateForm
    template_name = 'order/update_status_order_for_manager.html'
    success_url = reverse_lazy('order:order_list')
    permission_required = 'order.change_order'

    def get_queryset(self):
        return models.Order.objects


class ListOrderView(UserPassesTestMixin, generic.ListView):
    """Показываем список заказов"""
    model = models.Order
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')


class CancelOrderView(LoginRequiredMixin, generic.edit.UpdateView):
    """Отмена заказа для пользователя"""
    form_class = forms.OrderDeliveryStatusUpdateForm
    template_name = 'order/update_status_order.html'
    success_url = reverse_lazy('myaccount')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delivery_status = 3
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_queryset(self):
        return models.Order.objects


class OrderUpdateByPkView(LoginRequiredMixin, generic.edit.UpdateView):
    """Обновляем заказ по pk"""
    form_class = forms.OrderUpdateForm
    template_name = 'order/update_order.html'
    success_url = reverse_lazy('myaccount')

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        address_in_order = models.AddressInOrder.objects.create(order=self.object)
        address_id = self.request.POST.get('address')
        address_from_user = self.request.user.profile.profile_address.filter(pk=address_id).first()
        address_in_order.country = address_from_user.country
        address_in_order.city = address_from_user.city
        address_in_order.index = address_from_user.index
        address_in_order.address1 = address_from_user.address1
        address_in_order.address2 = address_from_user.address2
        address_in_order.save()
        type_of_payment_from_post = self.request.POST.get('paymentMethod')
        self.object.type_of_payment = type_of_payment_from_post
        cart_views.create_cart(self.request.user, self.request.session)
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            userdata = form.save(commit=False)
            userdata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form))

    def get_object(self, queryset=None):
        cart_id = self.request.session.get('cart_id')
        cart = cart_models.Cart.objects.filter(pk=cart_id).first()
        return cart.order


class UpdateOrderForManagerByPkView(PermissionRequiredMixin, generic.UpdateView):
    """Обновляем заказ для менеджера"""
    model = models.Order
    form_class = forms.OrderUpdateForManagersForm
    template_name = 'order/update_order_by_pk.html'
    success_url = '/order/order_list/'
    permission_required = 'order.update_order'
