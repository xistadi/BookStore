from django.contrib.auth import views
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.shortcuts import get_object_or_404, redirect

from . import forms, models
from cart.models import Cart


class MyLoginView(views.LoginView):
    pass

    def get_success_url(self):
        url = self.get_redirect_url()
        cart_id = self.request.session.get('cart_id')
        if cart_id:
            user = self.request.user
            cart = Cart.objects.filter(pk=cart_id).first()
            cart.customer = user
            cart.save()
        return url or reverse_lazy('myaccount')


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


class ProfileUpdateView(LoginRequiredMixin, generic.edit.UpdateView):
    """Обновляем профиль"""
    form_class = forms.UserUpdateForm
    second_form_class = forms.ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('myaccount')
    redirect_field_name = 'next'

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        return redirect_to

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object)
        context['form2'] = self.second_form_class(instance=self.request.user.profile)
        context.update({self.redirect_field_name: self.get_redirect_url()})
        return context

    def get(self, request, *args, **kwargs):
        super(ProfileUpdateView, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        form2 = self.second_form_class(request.POST, request.FILES, instance=self.request.user.profile)

        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            # used to set the password, but no longer necesarry
            userdata.save()
            employeedata = form2.save(commit=False)
            employeedata.user = userdata
            employeedata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form2=form2))

    def get_object(self):
        return self.request.user


class CreateProfileAddressView(LoginRequiredMixin, generic.CreateView):
    """Создаем адрес для профиля"""
    form_class = forms.ProfileAddressUpdateForm
    template_name = 'myauth/address_create.html'
    success_url = reverse_lazy('order:update_order')
    redirect_field_name = 'next'

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        return redirect_to

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(CreateProfileAddressView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context.update({self.redirect_field_name: self.get_redirect_url()})
        return super().get_context_data(**context)


class DeleteProfileAddressView(LoginRequiredMixin, generic.DeleteView):
    """Удаляем адрес из профиля"""
    template_name = 'myauth/address_delete.html'
    success_url = reverse_lazy('myaccount')

    def get_object(self, queryset=None):
        return get_object_or_404(models.ProfileAddress, pk=self.request.POST.get('pk'))


class UpdateProfileAddressView(LoginRequiredMixin, generic.UpdateView):
    """Обновляем адрес из профиля"""
    form_class = forms.ProfileAddressUpdateForm
    template_name = 'myauth/address_update.html'
    success_url = reverse_lazy('myaccount')
    redirect_field_name = 'next'

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        return redirect_to

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileAddressView, self).get_context_data(**kwargs)
        pk_from_url = self.kwargs.get('number') - 1
        try:
            self.request.user.profile.profile_address.all()[pk_from_url]
        except:
            raise Http404("Umg puk-puk")
        context['form'] = self.form_class(instance=self.request.user.profile.profile_address.all()[pk_from_url])
        context.update({self.redirect_field_name: self.get_redirect_url()})
        return context

    def get(self, request, *args, **kwargs):
        super(UpdateProfileAddressView, self).get(request, *args, **kwargs)
        form = self.form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            userdata = form.save(commit=False)
            userdata.profile = self.request.user.profile
            userdata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form))

    def get_object(self):
        pk_from_url = self.kwargs.get('number') - 1
        try:
            self.request.user.profile.profile_address.all()[pk_from_url]
        except:
            raise Http404("Umg puk-puk")
        return self.request.user.profile.profile_address.all()[pk_from_url]


class CreateCreditCartView(LoginRequiredMixin, generic.CreateView):
    """Создаем банк карту для профиля"""
    form_class = forms.CreditCardUpdateForm
    template_name = 'myauth/card_create.html'
    success_url = reverse_lazy('order:update_order')
    redirect_field_name = 'next'

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        return redirect_to

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(CreateCreditCartView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        """Insert the single object into the context dict."""
        context = {}
        if self.object:
            context['object'] = self.object
            context_object_name = self.get_context_object_name(self.object)
            if context_object_name:
                context[context_object_name] = self.object
        context.update(kwargs)
        context.update({self.redirect_field_name: self.get_redirect_url()})
        return super().get_context_data(**context)


class DeleteCreditCartView(LoginRequiredMixin, generic.DeleteView):
    """Удаляем банк карту для профиля"""
    template_name = 'myauth/card_delete.html'
    success_url = reverse_lazy('myaccount')

    def get_object(self, queryset=None):
        return get_object_or_404(models.CreditCart, pk=self.request.POST.get('pk'))


class ListProfileView(UserPassesTestMixin, generic.ListView):
    """Показываем список профилей"""
    queryset = models.Profile.objects.order_by('-pk')
    paginate_by = 10

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')


class ShowProfileByPkView(generic.DetailView):
    """Показываем профиль по pk"""
    model = models.Profile
    template_name = 'myauth/profile_by_pk.html'


class ProfileUpdateByPkView(UserPassesTestMixin, generic.edit.UpdateView):
    """Обновляем профиль по pk"""
    form_class = forms.UserUpdateForm
    second_form_class = forms.ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('myaccount')
    redirect_field_name = 'next'

    def get_redirect_url(self):
        redirect_to = self.request.POST.get(
            self.redirect_field_name,
            self.request.GET.get(self.redirect_field_name, '')
        )
        return redirect_to

    def get_success_url(self):
        url = self.get_redirect_url()
        return url

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateByPkView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object)
        context['form2'] = self.second_form_class(instance=self.request.user.profile)
        context.update({self.redirect_field_name: self.get_redirect_url()})
        return context

    def get(self, request, *args, **kwargs):
        super(ProfileUpdateByPkView, self).get(request, *args, **kwargs)
        form = self.form_class
        form2 = self.second_form_class
        return self.render_to_response(self.get_context_data(
            object=self.object, form=form, form2=form2))

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        form2 = self.second_form_class(request.POST, request.FILES, instance=self.object.profile)

        if form.is_valid() and form2.is_valid():
            userdata = form.save(commit=False)
            # used to set the password, but no longer necesarry
            userdata.save()
            employeedata = form2.save(commit=False)
            employeedata.user = userdata
            employeedata.save()
            return HttpResponseRedirect(self.get_success_url())
        else:
            return self.render_to_response(
                self.get_context_data(form=form, form2=form2))

    def get_queryset(self):
        return User.objects

    def test_func(self):
        return self.request.user.is_staff

    def handle_no_permission(self):
        return redirect('login')
