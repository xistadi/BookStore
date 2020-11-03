from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowReferencesView.as_view()),
    path('genre/', views.ShowGenreListView.as_view()),
    path('author/', views.ShowAuthorListView.as_view()),
    path('series/', views.ShowSeriesListView.as_view()),
    path('publisher/', views.ShowPublisherListView.as_view()),
    path('genre/<int:pk>/', views.ShowGenreByPkView.as_view()),
    path('author/<int:pk>/', views.ShowAuthorByPkView.as_view()),
    path('series/<int:pk>/', views.ShowSeriesByPkView.as_view()),
    path('publisher/<int:pk>/', views.ShowPublisherByPkView.as_view()),
    path('genre/create/', views.CreateGenreView.as_view()),
    path('author/create/', views.CreateAuthorView.as_view()),
    path('series/create/', views.CreateSeriesView.as_view()),
    path('publisher/create/', views.CreatePublisherView.as_view()),
    path('genre/update/<int:pk>', views.UpdateGenreView.as_view()),
    path('author/update/<int:pk>/', views.UpdateAuthorView.as_view()),
    path('series/update/<int:pk>/', views.UpdateSeriesView.as_view()),
    path('publisher/update/<int:pk>/', views.UpdatePublisherView.as_view()),
    path('genre/delete/<int:pk>/', views.DeleteGenreView.as_view()),
    path('author/delete/<int:pk>/', views.DeleteAuthorView.as_view()),
    path('series/delete/<int:pk>/', views.DeleteSeriesView.as_view()),
    path('publisher/delete/<int:pk>/', views.DeletePublisherView.as_view()),
]