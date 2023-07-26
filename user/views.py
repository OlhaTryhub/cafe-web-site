from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from user.forms import CustomUserCreationForm, UserUpdateForm
from user.models import User


class CreateUserView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "user/user_form.html"

    def get_success_url(self) -> str:
        return reverse("login")


class UserDetailView(generic.DetailView):
    model = User
    template_name = "user/user_detail.html"

    def get_object(self, queryset=None):
        return self.request.user


class UserUpdateView(generic.UpdateView):
    model = User
    form_class = UserUpdateForm

    def get_success_url(self) -> str:
        return reverse("user:user-detail")
