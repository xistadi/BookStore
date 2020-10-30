from django.urls import path
from . import views

urlpatterns = [
    path('<int:book_pk>/', views.show_book_by_pk_view),
    path('create/', views.create_book_view),
]