from django.urls import path
from . import views

app_name = 'references'

urlpatterns = [
    path('', views.ShowReferencesView.as_view(), name='reference_view'),
    path('genre/', views.ShowGenreListView.as_view(), name='genre_list'),
    path('author/', views.ShowAuthorListView.as_view(), name='author_list'),
    path('series/', views.ShowSeriesListView.as_view(), name='series_list'),
    path('publisher/', views.ShowPublisherListView.as_view(), name='publisher_list'),
    path('genre/<int:pk>/', views.ShowGenreByPkView.as_view(), name='genre_by_pk'),
    path('author/<int:pk>/', views.ShowAuthorByPkView.as_view(), name='author_by_pk'),
    path('series/<int:pk>/', views.ShowSeriesByPkView.as_view(), name='series_by_pk'),
    path('publisher/<int:pk>/', views.ShowPublisherByPkView.as_view(), name='publisher_by_pk'),
    path('genre/create/', views.CreateGenreView.as_view(), name='genre_create'),
    path('author/create/', views.CreateAuthorView.as_view(), name='author_create'),
    path('series/create/', views.CreateSeriesView.as_view(), name='series_create'),
    path('publisher/create/', views.CreatePublisherView.as_view(), name='publisher_create'),
    path('genre/update/<int:pk>', views.UpdateGenreView.as_view(), name='genre_update'),
    path('author/update/<int:pk>', views.UpdateAuthorView.as_view(), name='author_update'),
    path('series/update/<int:pk>', views.UpdateSeriesView.as_view(), name='series_update'),
    path('publisher/update/<int:pk>', views.UpdatePublisherView.as_view(), name='publisher_update'),
    path('genre/delete/<int:pk>/', views.DeleteGenreView.as_view(), name='genre_delete'),
    path('author/delete/<int:pk>/', views.DeleteAuthorView.as_view(), name='author_delete'),
    path('series/delete/<int:pk>/', views.DeleteSeriesView.as_view(), name='series_delete'),
    path('publisher/delete/<int:pk>/', views.DeletePublisherView.as_view(), name='publisher_delete'),
]