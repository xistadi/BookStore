from django.db import models


class Coupon(models.Model):
    name = models.CharField(
        'Название купона',
        max_length=9
    )
    percent = models.PositiveIntegerField(
        verbose_name='Процент скидки %'
    )
    active = models.BooleanField(
        verbose_name='Активный (Да/Нет)',
        default=True
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
        return f'Купон №{self.pk}, процент скидки: {self.percent}%, активный: {self.active}'

    class Meta:
        verbose_name = 'Купон'
        verbose_name_plural = 'Купоны'
