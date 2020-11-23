from django.urls import path
from . import views


urlpatterns = [
    path('', views.MyAccountView.as_view(), name='myaccount'),
    path('update/', views.ProfileUpdateView.as_view(), name='update_profile'),
    path('login/', views.MyLoginView.as_view(), name='login'),
    path('logout/', views.MyLogoutView.as_view(), name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('create_card/', views.CreateCreditCartView.as_view(), name='create_card'),
    path('delete_card/', views.DeleteCreditCartView.as_view(), name='delete_card'),
    path('create_address/', views.CreateProfileAddressView.as_view(), name='create_address'),
    path('delete_address/', views.DeleteProfileAddressView.as_view(), name='delete_address'),
    path('update_address/<int:number>/', views.UpdateProfileAddressView.as_view(), name='update_address'),
    path('password_reset/', views.MyPasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/', views.MyPasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_complete/', views.MyPasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('password_change/', views.MyPasswordChangeView.as_view(), name='password_change'),
    path('password_change_done/', views.MyPasswordChangeDoneView.as_view(), name='password_change_done'),
]
