# Generated by Django 4.2.3 on 2023-07-23 07:23

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dish", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="dish",
            name="photo",
            field=models.CharField(default="", max_length=255),
        ),
    ]
