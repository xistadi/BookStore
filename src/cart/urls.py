from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.CartView.as_view(), name='cart_index'),
    path('delete_book_in_cart/<int:pk>', views.DeleteBookInCart.as_view(), name='delete_book_in_cart'),
    path('update_cart', views.UpdateCart.as_view(), name='update_cart'),
]
