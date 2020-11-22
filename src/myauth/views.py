from django.contrib.auth import views
from django.views import generic
from django.http import HttpResponseRedirect, Http404
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404

from . import forms, models


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
    form_class = forms.UserUpdateForm
    second_form_class = forms.ProfileUpdateForm
    template_name = 'profile_update.html'
    success_url = reverse_lazy('myaccount')

    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        context['form'] = self.form_class(instance=self.object)
        context['form2'] = self.second_form_class(instance=self.request.user.profile)
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


class CreateProfileAddress(generic.CreateView):
    form_class = forms.ProfileAddressUpdateForm
    template_name = 'address_create.html'
    success_url = reverse_lazy('myaccount')

    def form_valid(self, form):
        form.instance.profile = self.request.user.profile
        return super(CreateProfileAddress, self).form_valid(form)


class DeleteProfileAddress(generic.DeleteView):
    template_name = 'address_delete.html'
    success_url = reverse_lazy('myaccount')

    def get_object(self, queryset=None):
        return get_object_or_404(models.ProfileAddress, pk=self.request.POST.get('pk'))


class UpdateProfileAddress(generic.UpdateView):
    form_class = forms.ProfileAddressUpdateForm
    template_name = 'address_update.html'
    success_url = reverse_lazy('myaccount')

    def get_context_data(self, **kwargs):
        context = super(UpdateProfileAddress, self).get_context_data(**kwargs)
        pk_from_url = self.kwargs.get('number') - 1
        try:
            self.request.user.profile.profile_address.all()[pk_from_url]
        except:
            raise Http404("Umg puk-puk")
        context['form'] = self.form_class(instance=self.request.user.profile.profile_address.all()[pk_from_url])
        return context

    def get(self, request, *args, **kwargs):
        super(UpdateProfileAddress, self).get(request, *args, **kwargs)
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
