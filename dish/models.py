from django.db import models


class MenuSection(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return f"{self.name}"


class DishType(models.Model):
    name = models.CharField(max_length=255)
    section = models.ForeignKey(to=MenuSection, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.name}"


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    photo = models.CharField(max_length=255, default="")
    type = models.ForeignKey(to=DishType, on_delete=models.DO_NOTHING)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "dishes"

    def __str__(self) -> str:
        return f"{self.name}, type({self.type.name}) price:{self.price}"
