from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Genre, Author, Series, Publisher
from . import forms as formimport


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
        form = formimport.CreateGenreForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = formimport.CreateGenreForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'genre'})


def create_author_view(request):
    if request.method == 'POST':
        form = formimport.CreateAuthorForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = formimport.CreateAuthorForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'author'})


def create_series_view(request):
    if request.method == 'POST':
        form = formimport.CreateSeriesForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = formimport.CreateSeriesForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'series'})


def create_publisher_view(request):
    if request.method == 'POST':
        form = formimport.CreatePublisherForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/references')
    else:
        form = formimport.CreatePublisherForm()
    return render(request, template_name='references/create_reference.html', context={'form': form, 'header': 'publisher'})


def update_genre_view(request, pk):
    if request.method == 'POST':
        form = formimport.UpdateGenreForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('name')
            ref_description = form.cleaned_data.get('description')
            obj = Genre.objects.get(pk=pk)
            obj.name = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Genre.objects.get(pk=pk)
        form = formimport.UpdateGenreForm(data={'name': ref.name, 'description': ref.description})
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'genre'})


def update_author_view(request, pk):
    if request.method == 'POST':
        form = formimport.UpdateAuthorForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('name')
            ref_description = form.cleaned_data.get('description')
            obj = Author.objects.get(pk=pk)
            obj.name = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Author.objects.get(pk=pk)
        form = formimport.UpdateAuthorForm(data={'name': ref.name, 'description': ref.description})
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'author'})


def update_series_view(request, pk):
    if request.method == 'POST':
        form = formimport.UpdateSeriesForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('name')
            ref_description = form.cleaned_data.get('description')
            obj = Series.objects.get(pk=pk)
            obj.name = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Series.objects.get(pk=pk)
        form = formimport.UpdateSeriesForm(data={'name': ref.name, 'description': ref.description})
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'series'})


def update_publisher_view(request, pk):
    if request.method == 'POST':
        form = formimport.UpdatePublisherForm(data=request.POST)
        if form.is_valid():
            ref_name = form.cleaned_data.get('name')
            ref_description = form.cleaned_data.get('description')
            obj = Publisher.objects.get(pk=pk)
            obj.name = ref_name
            obj.description = ref_description
            obj.save()
            return HttpResponseRedirect('/references')
    else:
        ref = Publisher.objects.get(pk=pk)
        form = formimport.UpdatePublisherForm(data={'name': ref.name, 'description': ref.description})
    return render(request, template_name='references/update_reference.html', context={'form': form, 'header': 'publisher'})


def delete_genre_view(request, pk):
    if request.method == 'POST':
        obj = Genre.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'genre'}
    return render(request, template_name='references/delete_reference.html', context=context)


def delete_author_view(request, pk):
    if request.method == 'POST':
        obj = Author.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'author'}
    return render(request, template_name='references/delete_reference.html', context=context)


def delete_series_view(request, pk):
    if request.method == 'POST':
        obj = Series.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'series'}
    return render(request, template_name='references/delete_reference.html', context=context)


def delete_publisher_view(request, pk):
    if request.method == 'POST':
        obj = Publisher.objects.get(pk=pk)
        obj.delete()
        return HttpResponseRedirect('/references')
    else:
        context = {'header': 'publisher'}
    return render(request, template_name='references/delete_reference.html', context=context)
