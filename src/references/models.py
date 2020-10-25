from django.db import models


class Genre(models.Model):
    name = models.CharField(
        'Название жанра',
        max_length=20,
    )
    description = models.TextField(
        'Описание жанра',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Жанр книги'
        verbose_name_plural = 'Жанры книги'


class Author(models.Model):
    name = models.CharField(
        'Имя автора',
        max_length=30,
    )
    description = models.TextField(
        'Описание автора',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Автор книги'
        verbose_name_plural = 'Авторы книги'


class Series(models.Model):
    name = models.CharField(
        'Название серии книг',
        max_length=20,
    )
    description = models.TextField(
        'Описание серии книг',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Серия книги'
        verbose_name_plural = 'Серии книги'


class Publisher(models.Model):
    name = models.CharField(
        'Название издательства',
        max_length=20,
    )
    description = models.TextField(
        'Описание издательства',
        blank=True,
        null=True
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Издательсво книги'
        verbose_name_plural = 'Издательства книги'
