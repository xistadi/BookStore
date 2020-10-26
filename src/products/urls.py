from django.urls import path
from .views import show_book_by_pk_view

urlpatterns = [
    path('<int:book_pk>/', show_book_by_pk_view),
]