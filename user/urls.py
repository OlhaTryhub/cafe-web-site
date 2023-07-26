from django.urls import path

from user.views import CreateUserView, UserDetailView, UserUpdateView

urlpatterns = [
    path("registration/", CreateUserView.as_view(), name="registration"),
    path("user_detail/", UserDetailView.as_view(), name="user-detail"),
    path("user_update/<int:pk>", UserUpdateView.as_view(), name="user-update")

]

app_name = "user"
