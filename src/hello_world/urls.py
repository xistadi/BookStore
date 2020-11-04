from django.urls import path
from . import views

urlpatterns = [
    path('', views.ShowBookListView.as_view(), name='index')
]