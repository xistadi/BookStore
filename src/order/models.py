from django.db import models
from cart import models as cart_models


class Order(models.Model):
    cart = models.OneToOneField(
        cart_models.Cart,
        related_name='order',
        on_delete=models.PROTECT
    )
    delivery_status_choices = (('1', 'В процессе оформления'), ('2', 'Заказан'), ('3', 'Доставка'),
                               ('4', 'Доставлен'))
    delivery_status = models.CharField(
        verbose_name='Статус заказа',
        default=1,
        max_length=20,
        choices=delivery_status_choices
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        blank=True,
        null=True
    )
    date_add = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name='Дата создания заказа'
    )
    date_last_change = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Дата последнего изменения заказа'
    )

    def __str__(self):
        return f'Заказ №{self.pk}, статус заказа: {self.get_delivery_status_display()}.'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
