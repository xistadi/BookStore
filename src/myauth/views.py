from django.contrib.auth import views
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import SignUpForm


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
