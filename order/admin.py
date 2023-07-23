from django.contrib import admin

from order.models import Order, OrderStatus, OrderDish

admin.site.register(Order)
admin.site.register(OrderStatus)
admin.site.register(OrderDish)
