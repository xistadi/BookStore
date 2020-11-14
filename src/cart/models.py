from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Cart(models.Model):
    customer = models.ForeignKey(
        User,
        related_name='carts',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        verbose_name='Пользователь'
    )
    date_add = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name='Дата добавления корзины'
    )
    date_last_change = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Дата последнего изменения корзины'
    )

    def __str__(self):
        return f'Корзина №{self.pk}, пользователь: {self.customer}.'

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'


class BookInCart(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        related_name='books'
    )
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество'
    )

    price = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        verbose_name='Цена',
    )

    def __str__(self):
        return f'Книги в корзине №{self.pk}, количество: {self.quantity}, цена: {self.price}.'

    class Meta:
        verbose_name = 'Книга в корзине'
        verbose_name_plural = 'Книги в корзине'
