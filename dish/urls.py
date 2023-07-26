from django.urls import path

from dish.views import (dish_type_view,
                        add_dish_to_users_order_view,
                        DishDetailView,
                        DishCreateView,
                        DishDeleteView,
                        DishUpdateView)

urlpatterns = [
    path("details/<int:pk>/", DishDetailView.as_view(), name="dish-detail"),
    path("details/<int:pk>/add_to_order/", add_dish_to_users_order_view, name="add-to-order"),
    path("create/", DishCreateView.as_view(), name="dish-create"),
    path("<int:pk>/delete/", DishDeleteView.as_view(), name="dish-delete"),
    path("<int:pk>/update/", DishUpdateView.as_view(), name="dish-update"),
    path("<str:dish_type>/", dish_type_view, name="dish-list"),
]

app_name = "dish"
