from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.core.exceptions import ValidationError

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

    # def clean_username(self) -> str:
    #     username = self.cleaned_data["username"].strip()
    #     if not username:
    #         raise ValidationError("Username can't be empy or contain only spaces!")
    #     elif len(username) < UserUpdateForm.MIN_USERNAME_LENGTH:
    #         raise ValidationError("Username must be longer than 4 symbols!")
    #     elif len(username) > UserUpdateForm.MAX_USERNAME_LENGTH:
    #         raise ValidationError("Username must be shorter than 16 symbols!")
    #     elif username.isnumeric():
    #         raise ValidationError("Username must not contain only numbers!")
    #     else:
    #         return username
    #

