from django.urls import path

from user.views import CreateUserView

urlpatterns = [
    path("registration/", CreateUserView.as_view(), name="registration"),
]

app_name = "user"
