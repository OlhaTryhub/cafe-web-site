from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from dish.models import Dish, DishType
from order.views import add_dish_to_users_order


def dish_type_view(request: HttpRequest, dish_type: str):
    dish_list = Dish.objects.filter(type__name=dish_type)
    type_obj = DishType.objects.filter(name=dish_type).first()
    section_name = type_obj.section.name
    type_list = DishType.objects.filter(section__name=section_name)

    context = {
        "dish_list": dish_list,
        "type_list": type_list,
        "section_name": section_name
    }

    return render(request, "dish/dish_list.html", context=context)


class DishDetailView(generic.DetailView):
    model = Dish


@login_required
def add_dish_to_users_order_view(request: HttpRequest,
                            pk: int) -> HttpResponseRedirect:
    _, dish_id = add_dish_to_users_order(request, pk)
    return HttpResponseRedirect(reverse_lazy("dish:dish-detail", args=[dish_id]))
