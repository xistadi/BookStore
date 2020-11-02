from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_references_view),
    path('genre/create/', views.create_genre_view),
    path('author/create/', views.create_author_view),
    path('series/create/', views.create_series_view),
    path('publisher/create/', views.create_publisher_view),
    path('genre/<int:pk>/update/', views.update_genre_view),
    path('author/<int:pk>/update/', views.update_author_view),
    path('series/<int:pk>/update/', views.update_series_view),
    path('publisher/<int:pk>/update/', views.update_publisher_view),
    path('genre/<int:pk>/delete/', views.delete_genre_view),
    path('author/<int:pk>/delete/', views.delete_author_view),
    path('series/<int:pk>/delete/', views.delete_series_view),
    path('publisher/<int:pk>/delete/', views.delete_publisher_view),
    path('<str:title>/<int:ref_pk>/', views.show_reference_by_pk_view),
]