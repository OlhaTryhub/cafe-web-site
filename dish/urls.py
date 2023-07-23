from django.urls import path

from dish.views import food_type_view

urlpatterns = [
    path("dish/<str:dish_type>/", food_type_view, name="food_list")
]

app_name = "dish"
