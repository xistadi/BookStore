from django.contrib.auth.views import LoginView, PasswordResetView


class MyLoginView(LoginView):
    pass


class MyPasswordResetView(PasswordResetView):
    pass
