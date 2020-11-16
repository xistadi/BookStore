from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.ShowBookListView.as_view()),
    path('<int:pk>/', views.ShowBookByPkView.as_view()),
    path('create/', views.CreateBookView.as_view()),
    path('update/<int:pk>/', views.UpdateBookView.as_view()),
    path('delete/<int:pk>/', views.DeleteBookView.as_view()),
    path('search/', views.SearchBookView.as_view(), name='search_results'),
]