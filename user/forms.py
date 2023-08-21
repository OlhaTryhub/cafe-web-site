from django.contrib.auth.forms import UserCreationForm
from django import forms

from user.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )


class UserUpdateForm(forms.ModelForm):
    MIN_USERNAME_LENGTH = 5
    MAX_USERNAME_LENGTH = 15

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ["username", "first_name", "last_name", "email"]
