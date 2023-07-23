from django.http import HttpRequest
from django.shortcuts import render
from django.views import generic

from dish.models import Dish, DishType


def food_type_view(request: HttpRequest, dish_type: str):
    dish_list = Dish.objects.filter(type__name=dish_type)
    type_obj = DishType.objects.get(name=dish_type)
    section_name = type_obj.section.name
    type_list = DishType.objects.filter(section__name=section_name)

    context = {
        "dish_list": dish_list,
        "type_list": type_list,
        "section_name": section_name
    }

    return render(request, "dish/dish_list.html", context=context)

