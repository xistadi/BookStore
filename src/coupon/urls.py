from django.urls import path
from . import views

app_name = 'coupon'

urlpatterns = [
    path('', views.ShowCouponListView.as_view(), name='list_coupon'),
    path('add_to_cart/', views.AddToCartCoupon.as_view(), name='add_to_cart'),
    path('create/', views.CreateCouponView.as_view(), name='create_coupon'),
    path('update/<int:pk>/', views.UpdateCouponView.as_view(), name='update_coupon'),
    path('delete/<int:pk>/', views.DeleteCouponView.as_view(), name='delete_coupon'),
    path('send_to_email/', views.SendCouponToEmail.as_view(), name='send_to_email'),
]
