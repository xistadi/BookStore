from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('update/', views.OrderUpdateView.as_view(), name='update_order'),
    path('update_status/<int:pk>', views.UpdateStatusOrderView.as_view(), name='update_order_status'),
    path('update_status_manager/<int:pk>', views.UpdateStatusOrderForManagerView.as_view(), name='update_order_status_manager'),
    path('order_list/', views.ListOrderView.as_view(), name='order_list'),
]
