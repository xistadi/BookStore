from django.db import models
from references.models import Author, Series, Genre, Publisher
from django.core.validators import MaxValueValidator, MinValueValidator

from django.urls import reverse_lazy


class Book(models.Model):
    name = models.CharField(
        'Название книги',
        max_length=50
    )
    photo = models.ImageField(
        verbose_name='Фото обложки',
        blank=True,
        null=True
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена (BYN)'
    )
    author = models.ManyToManyField(
        Author,
        verbose_name='Авторы книги',
        related_name='books'
    )

    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        verbose_name='Серия',
        related_name='books'
    )

    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры',
        related_name='books'
    )

    year = models.PositiveIntegerField(
        default=0,
        verbose_name='Год издания'
    )
    page = models.PositiveIntegerField(
        verbose_name="Страницы",
        default=0,
    )
    binding = models.CharField(
        'Переплет книги',
        max_length=30
    )
    book_format = models.CharField(
        'Формат книги',
        max_length=50
    )
    isbn = models.CharField(
        'ISBN',
        max_length=30
    )
    weight = models.PositiveIntegerField(
        'Вес книги(гр)',
        default=0,
    )
    age_limit = models.CharField(
        'Возрастное ограничение',
        max_length=5
    )
    publisher = models.ForeignKey(
        Publisher,
        on_delete=models.PROTECT,
        verbose_name='Издательство',
        related_name='books'
    )

    number_of_books = models.PositiveIntegerField(
        default=1,
        verbose_name='Количество книг в наличии'
    )
    active = models.BooleanField(
        verbose_name='Активный (доступен для заказа, Да/Нет)'
    )
    number_of_orders = models.PositiveIntegerField(
        default=0,
        verbose_name='Количество заказазов'
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
    avr_rating = models.SmallIntegerField(
        verbose_name='Средний рейтинг',
        default=0,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5)]
    )

    def get_rating(self):
        total = sum(int(comment['stars']) for comment in self.comments.values())

        if self.comments.count() > 0:
            return int(total / self.comments.count())
        else:
            return 0

    def __str__(self):
        return f'Книга №{self.pk}, имя: {self.name}.'

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
