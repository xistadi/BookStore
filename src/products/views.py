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
            ref_name = form.cleaned_data.get('name')
            ref_author = form.cleaned_data.get('author')
            ref_photo = request.FILES['photo']
            obj = Book.objects.get(pk=pk)
            obj.name = ref_name
            obj.description = ref_author
            obj.photo = ref_photo
            obj.save()
            return HttpResponseRedirect('/books')
    else:
        ref = Book.objects.get(pk=pk)
        form = formimport.UpdateBookForm(data={'name': ref.name, 'author': ref.author, 'photo': ref.photo,
                                               'price': ref.price, 'series': ref.series, 'genre': ref.genre,
                                               'year': ref.year, 'page': ref.page, 'binding': ref.binding,
                                               'book_format': ref.book_format, 'isbn': ref.isbn,
                                               'weight': ref.weight, 'age_limit': ref.age_limit,
                                               'publisher': ref.publisher, 'number_of_books': ref.number_of_books,
                                               'active': ref.active, 'rating': ref.rating, 'date_add': ref.date_add,
                                               'date_last_change': ref.date_last_change})
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
