from django.urls import path
from . import views

app_name = 'order'

urlpatterns = [
    path('update/<int:pk>', views.OrderUpdateView.as_view(), name='update_order'),
]
