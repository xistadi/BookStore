from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('update/', views.OrderUpdateView.as_view(), name='update_order'),
    path('update_status/<int:pk>', views.UpdateStatusOrderView.as_view(), name='update_order_status'),
]
