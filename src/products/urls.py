from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ShowBookListView.as_view(), name='book_list'),
    path('<int:pk>/', views.ShowBookByPkView.as_view(), name='book_by_pk'),
    path('create/', views.CreateBookView.as_view(), name='create_new_book'),
    path('update/<int:pk>/', views.UpdateBookView.as_view(), name='update_book_by_pk'),
    path('delete/<int:pk>/', views.DeleteBookView.as_view(), name='delete_book_by_pk'),
    path('search/', views.SearchBookView.as_view(), name='search_results'),
]