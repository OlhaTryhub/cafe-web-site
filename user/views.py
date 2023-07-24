from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic

from user.forms import CustomUserCreationForm
from user.models import User


class CreateUserView(generic.CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = "user/user_form.html"

    def get_success_url(self) -> str:
        return reverse("login")

