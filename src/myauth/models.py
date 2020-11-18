from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Profile(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.PROTECT,
        related_name='profile'
    )
    phone_number = models.CharField(
        'Номер телефона',
        max_length=20,
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
        return f'Профиль адрес №{self.pk}.'

    class Meta:
        verbose_name = 'Профиль адрес'
        verbose_name_plural = 'Профиль адреса'


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()
