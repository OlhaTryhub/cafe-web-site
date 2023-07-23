from django.contrib import admin

from dish.models import Dish, DishType, MenuSection

admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(MenuSection)
