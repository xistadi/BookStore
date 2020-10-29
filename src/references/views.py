from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Genre, Author, Series, Publisher
from .form import CreateGenreForm, CreateAuthorForm, CreatePublisherForm, CreateSeriesForm


def show_references_view(request):
    """Return a list of References obj"""
    genres = Genre.objects.all()
    authors = Author.objects.all()
    seriess = Series.objects.all()
    publishers = Publisher.objects.all()
    context = {'genres': genres, 'authors': authors, 'seriess': seriess, 'publishers': publishers}
    return render(request, template_name='references/ref_list.html', context=context)


def show_reference_by_pk_view(request, title, ref_pk):
    """Return Reference by pk obj"""
    if title == 'genre':
        type = Genre.objects.get(pk=ref_pk)
    elif title == 'author':
        type = Author.objects.get(pk=ref_pk)
    elif title == 'series':
        type = Series.objects.get(pk=ref_pk)
    elif title == 'publisher':
        type = Publisher.objects.get(pk=ref_pk)
    context = {'type': type}
    return render(request, template_name='references/ref.html', context=context)


def create_genre_view(request):
    if request.method == 'POST':
        form = CreateGenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateGenreForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'genre'})


def create_author_view(request):
    if request.method == 'POST':
        form = CreateAuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateAuthorForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'author'})


def create_series_view(request):
    if request.method == 'POST':
        form = CreateSeriesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreateSeriesForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'series'})


def create_publisher_view(request):
    if request.method == 'POST':
        form = CreatePublisherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = CreatePublisherForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'publisher'})
