from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('create/<int:pk>/', views.CreateCommentView.as_view(), name='create_comment'),
    path('delete/<int:pk>/', views.DeleteCommentView.as_view(), name='delete_comment'),
    path('update/<int:pk>/', views.UpdateCommentView.as_view(), name='update_comment'),
]
