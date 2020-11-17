from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        related_name='profile'
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=20,
        default=None
    )
    group = models.CharField(
        'Группа',
        max_length=20,
        default='User'
    )

    def __str__(self):
        return f'Профиль №{self.pk}.'

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class ProfileAddress(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.PROTECT,
        related_name='profile_address'
    )
    country = models.CharField(
        'Страна',
        max_length=20,
        default=None,
        blank=True,
        null=True
    )
    city = models.CharField(
        'Город',
        max_length=20,
        default=None,
        blank=True,
        null=True
    )
    index = models.CharField(
        'Индекс',
        max_length=15,
        default=None,
        blank=True,
        null=True
    )
    address1 = models.CharField(
        'Адрес1',
        max_length=50,
        default=None,
        blank=True,
        null=True
    )
    address2 = models.CharField(
        'Адрес2',
        max_length=50,
        default=None,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'Профиль адрес №{self.pk}.'

    class Meta:
        verbose_name = 'Профиль адрес'
        verbose_name_plural = 'Профиль адреса'
