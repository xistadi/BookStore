from django.shortcuts import render
from django.views.generic.base import View
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from . import models
from cart.models import Cart
from . import forms


class AddToCartCoupon(View):
    """Добавляем купон к корзине"""

    def post(self, request):
        user_promo = request.POST.get('promo')
        try:
            coupon = models.Coupon.objects.get(name=user_promo)
            if coupon.active:
                messages.success(request, 'Вы применили купон!')
                cart_id = self.request.session.get('cart_id')
                cart = Cart.objects.filter(pk=cart_id).first()
                cart.coupon_percent = coupon.percent
                cart.save()
            else:
                messages.error(request, 'Купон не активен!')
        except:
            messages.error(request, 'Такого купона не существует!')
        return redirect('/order/update/')


class CreateCouponView(PermissionRequiredMixin, CreateView):
    """Создаем новый купон"""
    models = models.Coupon
    template_name = 'coupon/create_coupon.html'
    form_class = forms.CreateCouponForm
    success_url = '/coupon/'
    permission_required = 'coupon.add_coupon'


class UpdateCouponView(PermissionRequiredMixin, UpdateView):
    """Обновляем купон"""
    model = models.Coupon
    form_class = forms.CreateCouponForm
    template_name = 'coupon/update_coupon.html'
    success_url = '/coupon/'
    permission_required = 'coupon.update_coupon'


class DeleteCouponView(PermissionRequiredMixin, DeleteView):
    """Удаляем купон"""
    model = models.Coupon
    success_url = '/coupon/'
    template_name = 'coupon/delete_coupon.html'
    permission_required = 'coupon.delete_coupon'


class ShowCouponListView(ListView):
    """Показываем список купонов"""
    model = models.Coupon
    paginate_by = 20
