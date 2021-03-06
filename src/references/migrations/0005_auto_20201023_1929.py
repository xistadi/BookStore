# Generated by Django 3.1.2 on 2020-10-23 16:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('references', '0004_publisher'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор книги', 'verbose_name_plural': 'Авторы книги'},
        ),
        migrations.AlterModelOptions(
            name='genre',
            options={'verbose_name': 'Жанр книги', 'verbose_name_plural': 'Жанры книги'},
        ),
        migrations.AlterModelOptions(
            name='publisher',
            options={'verbose_name': 'Издательсво книги', 'verbose_name_plural': 'Издательства книги'},
        ),
        migrations.AlterModelOptions(
            name='series',
            options={'verbose_name': 'Серия книги', 'verbose_name_plural': 'Серии книги'},
        ),
    ]
