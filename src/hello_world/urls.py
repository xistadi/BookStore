from django.urls import path
from . import views

app_name = 'index'

urlpatterns = [
    path('', views.ShowBookListView.as_view(), name='home'),
    path('sales/', views.ShowSales.as_view(), name='sales')
]