from django.urls import path

from dish.views import dish_type_view, DishDetailView

urlpatterns = [
    path("<str:dish_type>/", dish_type_view, name="dish-list"),
    path("details/<int:pk>/", DishDetailView.as_view(), name="dish-detail")
]

app_name = "dish"
