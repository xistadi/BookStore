from django.db import models
from cart import models as cart_models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Order(models.Model):
    cart = models.OneToOneField(
        cart_models.Cart,
        related_name='order',
        on_delete=models.PROTECT
    )
    delivery_status_choices = (('1', 'В процессе оформления'), ('2', 'На рассмотрении модерации'), ('3', 'Отменен'),
                               ('4', 'Заказан'), ('5', 'Доставка'), ('6', 'Доставлен'))
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
    type_of_payment = models.CharField(
        verbose_name='Тип оплаты',
        default=1,
        max_length=20
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


class AddressInOrder(models.Model):
    order = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='address_in_order'
    )
    country = models.CharField(
        'Страна',
        max_length=20,
        blank=True,
        null=True
    )
    city = models.CharField(
        'Город',
        max_length=20,
        blank=True,
        null=True
    )
    index = models.CharField(
        'Индекс',
        max_length=15,
        blank=True,
        null=True
    )
    address1 = models.CharField(
        'Адрес1',
        max_length=50,
        blank=True,
        null=True
    )
    address2 = models.CharField(
        'Адрес2',
        max_length=50,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Профиль адрес в заказе №{self.pk}.'

    class Meta:
        verbose_name = 'Профиль адрес в заказе'
        verbose_name_plural = 'Профиль адреса в заказах'
