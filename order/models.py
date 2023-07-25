from django.db import models
from dish.models import Dish
from user.models import User


class OrderStatus(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "order statuses"

    def __str__(self) -> str:
        return f"{self.name}"


class Order(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.ForeignKey(to=OrderStatus, on_delete=models.DO_NOTHING)
    dishes = models.ManyToManyField(to=Dish, through="OrderDish")
    making_datetime = models.DateTimeField()
    total_amount = models.PositiveIntegerField()
    address = models.CharField(max_length=255, blank=True)

    def __str__(self) -> str:
        return (f"{self.id} Status: {self.status.name} "
                f"creating at: {self.making_datetime}")


class OrderDish(models.Model):
    dish = models.ForeignKey(to=Dish, on_delete=models.DO_NOTHING)
    order = models.ForeignKey(to=Order, on_delete=models.CASCADE)
    dish_count = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "dishes in order"

    def __str__(self) -> str:
        return f"Order id: {self.order.id}: {self.dish.name} " \
               f"amount: {self.dish_count}"
