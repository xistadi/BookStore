from django.urls import path
from . import views

urlpatterns = [
    path('', views.show_references_view),
    path('genre/create/', views.create_genre_view),
    path('author/create/', views.create_author_view),
    path('series/create/', views.create_series_view),
    path('publisher/create/', views.create_publisher_view),
    path('<str:title>/<int:ref_pk>/', views.show_reference_by_pk_view),
]