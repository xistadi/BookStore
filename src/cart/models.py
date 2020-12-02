from django.db import models
from django.contrib.auth import get_user_model
from products import models as products_models

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
    coupon_percent = models.PositiveIntegerField(
        verbose_name='Процент скидки %',
        default=0
    )

    def total_price(self):
        price = 0
        for book_in_cart in self.books.all():
            price += book_in_cart.price
        if self.coupon_percent != 0:
            price = price - ((price * self.coupon_percent)/100)
        return price

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
    book = models.ForeignKey(
        products_models.Book,
        on_delete=models.PROTECT,
        related_name='books_in_carts'
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

    def construct_price(self):
        # some logic on sale and smthng
        return self.quantity * self.book.price

    def __str__(self):
        return f'Книги в корзине №{self.pk}, количество: {self.quantity}, цена: {self.price}.'

    class Meta:
        verbose_name = 'Книга в корзине'
        verbose_name_plural = 'Книги в корзине'
