from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import QuerySet
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views import generic

from dish.models import Dish
from order.forms import OrderConfirmByUserForm
from order.models import Order, OrderStatus, OrderDish
from user.models import User


def get_or_create_order_credentials(request: HttpRequest, pk: int) -> dict:
    user = User.objects.get(id=request.user.id)
    status = OrderStatus.objects.filter(name="creation").first()
    order = Order.objects.filter(user=user, status=status).first()
    dish = Dish.objects.get(id=pk)
    order_dish = OrderDish.objects.filter(dish=dish, order=order).first()
    return {
        "user": user,
        "status": status,
        "order": order,
        "dish": dish,
        "order_dish": order_dish
    }


def add_dish_to_users_order(request: HttpRequest,
                            pk: int) -> tuple:
    queryset_dict = get_or_create_order_credentials(request, pk)

    if not queryset_dict["order"]:
        queryset_dict["order"] = Order.objects.create(
            user=queryset_dict["user"],
            status=queryset_dict["status"],
            making_datetime=datetime.now(),
            total_amount=0
        )
    if not queryset_dict["order_dish"]:
        queryset_dict["order_dish"] = OrderDish.objects.create(
            dish=queryset_dict["dish"],
            order=queryset_dict["order"],
            dish_count=1
        )
    else:
        queryset_dict["order_dish"].dish_count = queryset_dict[
                                                     "order_dish"
                                                 ].dish_count + 1
        queryset_dict["order_dish"].save()
    queryset_dict["order"].total_amount += queryset_dict["dish"].price
    queryset_dict["order"].save()
    return queryset_dict["order"].id, queryset_dict["dish"].id


class OrderListView(LoginRequiredMixin, generic.ListView):
    model = Order
    template_name = "order/order_list.html"
    context_object_name = "order_list"

    def get_queryset(self) -> QuerySet:
        user = User.objects.get(id=self.request.user.id)
        queryset = Order.objects.filter(user=user).order_by("status")
        return queryset


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = "order/order_detail.html"
    queryset = Order.objects.prefetch_related("dishes")


@login_required
def add_dish_to_users_order_view(request: HttpRequest,
                                 pk: int) -> HttpResponseRedirect:
    order_id, _ = add_dish_to_users_order(request, pk)
    if order_id:
        return HttpResponseRedirect(reverse_lazy("order:order-detail", args=[order_id]))
    else:
        return HttpResponseRedirect(reverse_lazy("order:order-list"))


@login_required
def remove_dish_from_users_order_view(request: HttpRequest,
                                      pk: int) -> HttpResponseRedirect:
    queryset_dict = get_or_create_order_credentials(request, pk)
    queryset_dict["order_dish"].dish_count -= 1
    queryset_dict["order_dish"].save()
    queryset_dict["order"].total_amount -= queryset_dict["dish"].price
    queryset_dict["order"].save()
    if queryset_dict["order_dish"].dish_count == 0:
        queryset_dict["order_dish"].delete()
        if not OrderDish.objects.filter(order=queryset_dict["order"]):
            queryset_dict["order"].delete()
            return HttpResponseRedirect(reverse_lazy("order:order-list"))
    return HttpResponseRedirect(reverse_lazy("order:order-detail", args=[queryset_dict["order"].id]))


class OrderConfirmByUserView(LoginRequiredMixin, generic.UpdateView):
    model = Order
    form_class = OrderConfirmByUserForm
    template_name = 'order/order_detail.html'

    def get_object(self, queryset=None):
        return get_object_or_404(Order, pk=self.kwargs.get('pk'))

    def get_success_url(self):
        return reverse('order:order-detail', kwargs={'pk': self.object.pk})

    def form_valid(self, form):
        self.object.status = OrderStatus.objects.filter(name="processing").first()
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())
