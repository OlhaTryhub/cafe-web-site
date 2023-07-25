from django.urls import path

from dish.views import dish_type_view, DishDetailView, add_dish_to_users_order_view

urlpatterns = [
    path("<str:dish_type>/", dish_type_view, name="dish-list"),
    path("details/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("details/<int:pk>/add_to_order/", add_dish_to_users_order_view, name="add-to-order"),
]

app_name = "dish"
