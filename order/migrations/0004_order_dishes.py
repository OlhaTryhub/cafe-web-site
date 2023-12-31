# Generated by Django 4.2.3 on 2023-07-25 12:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dish", "0003_alter_dish_price"),
        ("order", "0003_alter_order_total_amount"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="dishes",
            field=models.ManyToManyField(through="order.OrderDish", to="dish.dish"),
        ),
    ]
