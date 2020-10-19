from django.db import models
from references.models import Author, Series, Genre, Publisher

class Book(models.Model):
    name = models.CharField(
        'Название книги',
        max_length=50
    )
    photo = models.ImageField(
    verbose_name='Фото обложки'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена (BYN)'
    )
    author = models.ManyToManyField(
        Author,
        verbose_name='Авторы книги'
    )

    series = models.ForeignKey(
        Series,
        on_delete=models.PROTECT,
        verbose_name='Серия'
    )

    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанры'
    )

    year = models.IntegerField(
        default=0,
        verbose_name='Год издания'
    )
    page = models.IntegerField(
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
    weight = models.IntegerField(
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
        verbose_name='Издательство'
    )

    number_of_books = models.IntegerField(
        default=1,
        verbose_name='Количество книг в наличии'
    )
    active = models.BooleanField(
        verbose_name='Активный (доступен для заказа, Да/Нет)'
    )
    rating = models.IntegerField(
        default=0,
        verbose_name='Рейтинг (0 - 10)'
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
        return self.name
