from .models import Genre, Author, Series, Publisher
from products.models import Book
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from . import forms


class ShowReferencesView(TemplateView):
    template_name = 'references/all_references_list.html'

    def get_context_data(self, **kwargs):
        genres = Genre.objects.all()
        authors = Author.objects.all()
        seriess = Series.objects.all()
        publishers = Publisher.objects.all()
        context = super().get_context_data(**kwargs)
        context['genres'] = genres
        context['authors'] = authors
        context['seriess'] = seriess
        context['publishers'] = publishers
        return context


class ShowGenreListView(ListView):
    model = Genre
    template_name = 'references/ref_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Жанры книг'
        return context


class ShowAuthorListView(ListView):
    model = Author
    template_name = 'references/ref_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Авторы книг'
        return context


class ShowSeriesListView(ListView):
    model = Series
    template_name = 'references/ref_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Серии книг'
        return context


class ShowPublisherListView(ListView):
    model = Publisher
    template_name = 'references/ref_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'Издательства книг'
        return context


class ShowGenreByPkView(DetailView, MultipleObjectMixin):
    model = Genre
    paginate_by = 5
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(genre=self.get_object())
        context = super(ShowGenreByPkView, self).get_context_data(object_list=object_list, **kwargs)
        context['type'] = 'genre'
        return context


class ShowAuthorByPkView(DetailView, MultipleObjectMixin):
    model = Author
    paginate_by = 5
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(author=self.get_object())
        context = super(ShowAuthorByPkView, self).get_context_data(object_list=object_list, **kwargs)
        context['type'] = 'author'
        return context


class ShowSeriesByPkView(DetailView, MultipleObjectMixin):
    model = Series
    paginate_by = 5
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(series=self.get_object())
        context = super(ShowSeriesByPkView, self).get_context_data(object_list=object_list, **kwargs)
        context['type'] = 'series'
        return context


class ShowPublisherByPkView(DetailView, MultipleObjectMixin):
    model = Publisher
    paginate_by = 5
    template_name = 'references/ref_by_pk.html'

    def get_context_data(self, **kwargs):
        object_list = Book.objects.filter(publisher=self.get_object())
        context = super(ShowPublisherByPkView, self).get_context_data(object_list=object_list, **kwargs)
        context['type'] = 'publisher'
        return context


class CreateGenreView(PermissionRequiredMixin, CreateView):
    model = Genre
    form_class = forms.CreateGenreForm
    template_name = 'references/create_reference.html'
    success_url = '/references/genre'
    permission_required = 'refereces.add_genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'жанр'
        return context


class CreateAuthorView(PermissionRequiredMixin, CreateView):
    model = Author
    form_class = forms.CreateAuthorForm
    template_name = 'references/create_reference.html'
    success_url = '/references/author'
    permission_required = 'refereces.add_author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'автора'
        return context


class CreateSeriesView(PermissionRequiredMixin, CreateView):
    model = Series
    form_class = forms.CreateSeriesForm
    template_name = 'references/create_reference.html'
    success_url = '/references/series'
    permission_required = 'refereces.add_series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'серию'
        return context


class CreatePublisherView(PermissionRequiredMixin, CreateView):
    model = Publisher
    form_class = forms.CreatePublisherForm
    template_name = 'references/create_reference.html'
    success_url = '/references/publisher'
    permission_required = 'refereces.add_publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'издательство'
        return context


class UpdateGenreView(PermissionRequiredMixin, UpdateView):
    model = Genre
    form_class = forms.UpdateGenreForm
    success_url = '/references/genre'
    template_name = 'references/update_reference.html'
    permission_required = 'refereces.change_genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'жанр'
        return context


class UpdateAuthorView(PermissionRequiredMixin, UpdateView):
    model = Author
    form_class = forms.UpdateAuthorForm
    success_url = '/references/author'
    template_name = 'references/update_reference.html'
    permission_required = 'refereces.change_author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'автора'
        return context


class UpdateSeriesView(PermissionRequiredMixin, UpdateView):
    model = Series
    form_class = forms.UpdateSeriesForm
    success_url = '/references/series'
    template_name = 'references/update_reference.html'
    permission_required = 'refereces.change_series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'серию'
        return context


class UpdatePublisherView(PermissionRequiredMixin, UpdateView):
    model = Publisher
    form_class = forms.UpdatePublisherForm
    success_url = '/references/publisher'
    template_name = 'references/update_reference.html'
    permission_required = 'refereces.change_publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'издательство'
        return context


class DeleteGenreView(PermissionRequiredMixin, DeleteView):
    model = Genre
    success_url = '/references/genre'
    template_name = 'references/delete_reference.html'
    permission_required = 'refereces.delete_genre'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'жанр'
        return context


class DeleteAuthorView(PermissionRequiredMixin, DeleteView):
    model = Author
    success_url = '/references/author'
    template_name = 'references/delete_reference.html'
    permission_required = 'refereces.delete_author'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'автора'
        return context


class DeleteSeriesView(PermissionRequiredMixin, DeleteView):
    model = Series
    success_url = '/references/series'
    template_name = 'references/delete_reference.html'
    permission_required = 'refereces.delete_series'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'серию'
        return context


class DeletePublisherView(PermissionRequiredMixin, DeleteView):
    model = Publisher
    success_url = '/references/publisher'
    template_name = 'references/delete_reference.html'
    permission_required = 'refereces.delete_publisher'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['header'] = 'издательство'
        return context
