# Generated by Django 3.1.2 on 2020-10-19 20:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('references', '0004_publisher'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Название книги')),
                ('photo', models.ImageField(upload_to=None)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('year', models.IntegerField(default=0)),
                ('page', models.IntegerField(default=0)),
                ('binding', models.CharField(max_length=20, verbose_name='Переплет книги')),
                ('book_format', models.CharField(max_length=10, verbose_name='Формат книги')),
                ('isbn', models.CharField(max_length=10, verbose_name='ISBN')),
                ('weight', models.CharField(max_length=5, verbose_name='Вес книги(гр)')),
                ('age_limit', models.CharField(max_length=5, verbose_name='Возрастное ограничение')),
                ('number_of_books', models.IntegerField(default=0)),
                ('active', models.BooleanField()),
                ('rating', models.DecimalField(decimal_places=0, max_digits=2)),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_last_change', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to='references.Author')),
                ('genre', models.ManyToManyField(to='references.Genre')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='references.publisher')),
                ('series', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='references.series')),
            ],
        ),
    ]