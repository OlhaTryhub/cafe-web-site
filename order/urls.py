from django.urls import path

from order.views import (add_dish_to_users_order_view,
                         remove_dish_from_users_order_view,
                         OrderListView,
                         OrderDetailView,
                         OrderConfirmByUserView)

urlpatterns = [
    path("order_list/", OrderListView.as_view(), name="order-list"),
    path("order_detail/<int:pk>/", OrderDetailView.as_view(), name="order-detail"),
    path("order_detail/<int:pk>/add_dish/", add_dish_to_users_order_view, name="order-detail-add"),
    path("<int:pk>/remove_dish/", remove_dish_from_users_order_view, name="order-detail-remove"),
    path("order_detail/<int:pk>/confirm_by_user/", OrderConfirmByUserView.as_view(), name="confirm-order-by-user"),
]

app_name = "order"
