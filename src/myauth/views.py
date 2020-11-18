from django.contrib.auth import views
from django.views import generic
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from . import forms


class MyLoginView(views.LoginView):
    pass


class MyLogoutView(views.LogoutView):
    template_name = 'logout.html'


class MyPasswordResetView(views.PasswordResetView):
    template_name = 'password_reset.html'


class MyPasswordResetDoneView(views.PasswordResetDoneView):
    template_name = 'password_reset_done.html'


class MyPasswordResetCompleteView(views.PasswordResetCompleteView):
    template_name = 'password_reset_complete.html'


class MyPasswordChangeView(views.PasswordChangeView):
    template_name = 'password_change.html'


class MyPasswordChangeDoneView(views.PasswordChangeDoneView):
    template_name = 'password_change_done.html'


class SignUpView(generic.CreateView):
    form_class = forms.SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


class MyAccountView(LoginRequiredMixin, views.TemplateView):
    template_name = 'my_account.html'


class ProfileUpdateView(generic.edit.UpdateView):
    form_class = forms.ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('myaccount')

    def get_object(self):
        return self.request.user
