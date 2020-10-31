from django.shortcuts import render
from django.http import HttpResponseRedirect
from . import forms as formimport
from .models import Book


def show_books_view(request):
    """Return a list of Books obj"""
    books = Book.objects.all()
    context = {'books': books}
    return render(request, template_name='products/book_list.html', context=context)


def show_book_by_pk_view(request, book_pk):
    """Return Book obj by pk"""
    name = Book.objects.get(pk=book_pk).name
    price = Book.objects.get(pk=book_pk).price
    author = Book.objects.get(pk=book_pk).author
    series = Book.objects.get(pk=book_pk).series
    genre = Book.objects.get(pk=book_pk).genre
    year = Book.objects.get(pk=book_pk).year
    context = {'name': name, 'price': price, 'author': author, 'series': series, 'genre': genre, 'year': year}
    return render(request, template_name='products/book.html', context=context)


def create_book_view(request):
    """Create new Book obj"""
    if request.method == 'POST':
        form = formimport.CreateBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/books')
    else:
        form = formimport.CreateBookForm()
    return render(request, template_name='products/create_book.html', context={'form': form, 'header': 'book'})


def update_book_view(request, pk):
    """Update Book obj by pk"""
    if request.method == 'POST':
        form = formimport.UpdateBookForm(request.POST, request.FILES)
        if form.is_valid():
            get_name = form.cleaned_data.get('name')
            get_price = form.cleaned_data.get('price')
            get_author = form.cleaned_data.get('author')
            get_series = form.cleaned_data.get('series')
            get_genre = form.cleaned_data.get('genre')
            get_year = form.cleaned_data.get('year')
            get_page = form.cleaned_data.get('page')
            get_binding = form.cleaned_data.get('binding')
            get_book_format = form.cleaned_data.get('book_format')
            get_isbn = form.cleaned_data.get('isbn')
            get_weight = form.cleaned_data.get('weight')
            get_age_limit = form.cleaned_data.get('age_limit')
            get_publisher = form.cleaned_data.get('publisher')
            get_number_of_books = form.cleaned_data.get('number_of_books')
            get_active = form.cleaned_data.get('active')
            get_rating = form.cleaned_data.get('rating')
            obj = Book.objects.get(pk=pk)
            obj.name = get_name
            obj.price = get_price
            obj.author.set(get_author)
            obj.series = get_series
            obj.genre.set(get_genre)
            obj.year = get_year
            obj.page = get_page
            obj.binding = get_binding
            obj.book_format = get_book_format
            obj.isbn = get_isbn
            obj.weight = get_weight
            obj.age_limit = get_age_limit
            obj.publisher = get_publisher
            obj.number_of_books = get_number_of_books
            obj.active = get_active
            obj.rating = get_rating
            if 'photo' in request.FILES:
                get_photo = request.FILES['photo']
                obj.photo = get_photo
            obj.save()
            return HttpResponseRedirect('/books')
    else:
        book = Book.objects.get(pk=pk)
        form = formimport.UpdateBookForm(instance=book)
    return render(request, template_name='products/update_book.html', context={'form': form, 'header': 'book'})


def delete_book_view(request, pk):
    """Delete Book obj by pk"""
    if request.method == 'POST':
        obj = Book.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/books')
    else:
        context = {'header': 'book'}
    return render(request, template_name='products/delete_book.html', context=context)
