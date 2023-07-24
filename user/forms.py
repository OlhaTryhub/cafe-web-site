from django.contrib.auth.forms import UserCreationForm

from user.models import User


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + (
            "first_name",
            "last_name",
            "email",
        )
