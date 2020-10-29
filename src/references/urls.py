from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_references_view),
    path('genre/create/', views.create_genre_view),
    path('author/create/', views.create_author_view),
    path('series/create/', views.create_series_view),
    path('publisher/create/', views.create_publisher_view),
    path('genre/update/<int:pk>/', views.update_genre_view),
    path('author/update/<int:pk>/', views.update_author_view),
    path('series/update/<int:pk>/', views.update_series_view),
    path('publisher/update/<int:pk>/', views.update_publisher_view),
    path('genre/delete/<int:pk>/', views.delete_genre_view),
    path('author/delete/<int:pk>/', views.delete_author_view),
    path('series/delete/<int:pk>/', views.delete_series_view),
    path('publisher/delete/<int:pk>/', views.delete_publisher_view),
    path('<str:title>/<int:ref_pk>/', views.show_reference_by_pk_view),
]