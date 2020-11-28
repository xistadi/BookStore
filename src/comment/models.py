from django.db import models

from myauth import models as myauth_models
from products.models import Book


class CommentProducts(models.Model):
    profile = models.ForeignKey(
        myauth_models.Profile,
        on_delete=models.PROTECT,
        related_name='comments'
    )
    book = models.ForeignKey(
        Book,
        on_delete=models.PROTECT,
        related_name='comments'
    )
    comment = models.TextField(
        verbose_name='Комментарий',
        default='',
        blank=True,
        null=True
    )
    date_add = models.DateTimeField(
        auto_now=False,
        auto_now_add=True,
        verbose_name='Дата внесения в каталог'
    )
    date_last_change = models.DateTimeField(
        auto_now=True,
        auto_now_add=False,
        verbose_name='Дата последнего изменения карточки'
    )

    def __str__(self):
        return f'Комментарий №{self.pk}, пользователя: {self.profile}, к книге: {self.book}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
