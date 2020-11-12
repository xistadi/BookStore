from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# class CartProduct(models.Model):
#
#     user = models.ForeignKey('Customer', verbose_name='Покупатель', on_delete=models.CASCADE)
#     cart = models.ForeignKey('Cart', verbose_name='Корзина', on_delete=models.CASCADE, related_name='related_products')
#     object_id = models.PositiveIntegerField()
#     qty = models.PositiveIntegerField(default=1)
#     final_price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Общая цена')
#
#     def __str__(self):
#         return "Продукт: {} (для корзины)".format(self.content_object.title)
#
#     def save(self, *args, **kwargs):
#         self.final_price = self.qty * self.content_object.price
#         super().save(*args, **kwargs)
#
#
# class Cart(models.Model):
#
#     owner = models.ForeignKey('Customer', null=True, verbose_name='Владелец', on_delete=models.CASCADE)
#     products = models.ManyToManyField(CartProduct, blank=True, related_name='related_cart')
#     total_products = models.PositiveIntegerField(default=0)
#     final_price = models.DecimalField(max_digits=9, default=0, decimal_places=2, verbose_name='Общая цена')
#     in_order = models.BooleanField(default=False)
#     for_anonymous_user = models.BooleanField(default=False)
#
#     def __str__(self):
#         return str(self.id)
#
#
# class Customer(models.Model):
#
#     user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
#     phone = models.CharField(max_length=20, verbose_name='Номер телефона', null=True, blank=True)
#     address = models.CharField(max_length=255, verbose_name='Адрес', null=True, blank=True)
#     orders = models.ManyToManyField('Order', verbose_name='Заказы покупателя', related_name='related_order')
#
#     def __str__(self):
#         return "Покупатель: {} {}".format(self.user.first_name, self.user.last_name)
