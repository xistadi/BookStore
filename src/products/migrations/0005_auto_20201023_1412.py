# Generated by Django 3.1.2 on 2020-10-23 11:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_publisher'),
        ('products', '0004_auto_20201020_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author',
            field=models.ManyToManyField(related_name='books', to='references.Author', verbose_name='Авторы книги'),
        ),
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ManyToManyField(related_name='books', to='references.Genre', verbose_name='Жанры'),
        ),
        migrations.AlterField(
            model_name='book',
            name='number_of_books',
            field=models.PositiveIntegerField(default=1, verbose_name='Количество книг в наличии'),
        ),
        migrations.AlterField(
            model_name='book',
            name='page',
            field=models.PositiveIntegerField(default=0, verbose_name='Страницы'),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='references.publisher', verbose_name='Издательство'),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.PositiveIntegerField(default=0, verbose_name='Рейтинг (0 - 10)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='series',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='books', to='references.series', verbose_name='Серия'),
        ),
        migrations.AlterField(
            model_name='book',
            name='weight',
            field=models.PositiveIntegerField(default=0, verbose_name='Вес книги(гр)'),
        ),
        migrations.AlterField(
            model_name='book',
            name='year',
            field=models.PositiveIntegerField(default=0, verbose_name='Год издания'),
        ),
    ]
